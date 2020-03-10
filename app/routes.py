from flask import render_template, redirect, url_for, request, g
from flask_restful import Api
from app import app, blog, header
from app.resources import HelloWorldResource, MultiResource, ComponentResource
import requests
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.embed import components
from app.forms import create_position_form
from app.utilities import get_component_range
import json

'''
**********************************
* Application Routes Definition  *
**********************************
'''
# Home Page
@app.route('/')
@app.route('/index')
def index():
    header['label'] = 'Jeep Python Flask RestFul App'
    return render_template('index.html', title='Home', header=header)

# Plot Page using Bokey plotting   
@app.route('/plot', methods=['GET', 'POST'])
def plot():
    header['label'] = 'Plotting with Bokey'
    rangePosition = get_component_range() 
    skeys = sorted(rangePosition.keys())
    rangeKeys = {'min': skeys[0],'max': skeys[-1]}

    # create the form to select the Position option
    form = create_position_form(rangePosition[skeys[0]],rangePosition[skeys[-1]])
    plots = []
    # on submit make the plot
    if form.validate_on_submit():
        plots.append(make_plot(form))

    return render_template('plot.html', title='Plot', 
        message='', form=form, plots=plots, data=rangePosition,
        rangeKeys=rangeKeys, header=header)

# About Page
@app.route('/about')
def about():
    header['label'] = 'About Me'
    return render_template('about.html', title='About', header=header)

@app.route('/newplot/<string:pos>', methods=['GET', 'POST'])
def newplot(pos):
    header['label'] = 'Plotting with Web Component'
    message = ''
    rangePosition = get_component_range() 
    skeys = sorted(rangePosition.keys())
    rangeKeys = {'min': skeys[0],'max': skeys[-1]}
    plots = []
    mode = 'none'
    # on pos != none make the plot
    if pos != 'none':
        # parse string to json
        jsonPos = eval(pos) 
        mode = jsonPos['mode']
        plots.append(make_newplot(jsonPos))

    return render_template('newplot.html', title='NewPlot', 
        message=message, plots=plots, data=rangePosition,
        mode=mode, rangeKeys=rangeKeys, header=header)


'''
********************************
* Application Private Methods  *
********************************
'''

def make_plot(form):
    plot_title = "Component Weight versus Position "
    if form.sel_option.data == "All" :
        payload = {}
        plot_title = plot_title + ': All'
    elif form.sel_option.data == "One" :
        payload = {'position':int(form.sel_from.data)}
        plot_title = plot_title + ': ' + form.sel_from.data
    elif form.sel_option.data == "From" :
        payload = {'filter':'position','from':int(form.sel_from.data)}
        plot_title = plot_title + 'from : ' + form.sel_from.data
    elif form.sel_option.data == "To" :
        payload = {'filter':'position','to':int(form.sel_to.data)}
        plot_title = plot_title + 'to : ' + form.sel_to.data
    elif form.sel_option.data == "FromTo" :
        payload = {'filter':'position','from':int(form.sel_from.data),'to':int(form.sel_to.data)}
        plot_title = plot_title + 'from : ' + form.sel_from.data + ' to : ' + form.sel_to.data
    else :
        payload = {}
        plot_title = plot_title + ': All'
    # make the request to the restful api
    if len(payload) == 0 :
        r= requests.get('http://localhost:5000/component')
    else :
        r= requests.get('http://localhost:5000/component',params=payload)
    # convert response to list
    # r.json() is {'Components': [{'id': 5, 'position': 8, 'weight': 3.75},...]}
    lcp = list(r.json().values())[0]
    # create data for ColumnDataSource
    position = []
    weight = []
    for cp in lcp:
        position.append(cp['position'])
        weight.append(cp['weight'])
    source = ColumnDataSource(data={
        'position' : position,
        'weight' : weight
    })
    # create the plot with Bokeh 
    plot = figure(plot_height=300, sizing_mode='scale_width',x_axis_label = "Position",
       y_axis_label = "Weight")
    if(form.sel_option.data == "One") :
        plot.circle(x='position', y='weight', source=source, size=10, color="navy", alpha=0.5)
    else :
        plot.line(x='position', y='weight', source=source, line_width=3)
    plot.title.text = plot_title
    plot.title.align = "center"
    plot.title.text_color = "blue"
    plot.title.text_font_size = "25px"
    script, div = components(plot)
    return script, div

def make_newplot(data):
    plot = {}
    payload = {}
#   set the plot title, subtitle, x-axis title and y-axis title
    plot['title'] = "Component Weight versus Position"
    plot['x_axis_label'] = "Position"
    plot['y_axis_label'] = "Weight"
    if data['mode'] == "all" :
        payload = {}
        plot['sub_title'] = "Position: " + "All"
    elif data['mode'] == "one" :
        payload = {'position':int(data['value']['from'])}
        plot['sub_title'] = "Position: " + str(data['value']['from'])
    elif data['mode'] == "from" :
        payload = {'filter':'position','from':int(data['value']['from'])}
        plot['sub_title'] = "Position From: " + str(data['value']['from'])
    elif data['mode'] == "to" :
        payload = {'filter':'position','to':int(data['value']['to'])}
        plot['sub_title'] = "Position To: " + str(data['value']['to'])
    elif data['mode'] == "fromto" :
        payload = {'filter':'position','from':int(data['value']['from']),
            'to':int(data['value']['to'])}
        plot['sub_title'] = "Position From: " + str(data['value']['from']) \
            + " To: " + str(data['value']['to'])            
    else :
        payload = {}
        plot['sub_title'] = "Position: " + "All"

    # make the request to the restful api
    if len(payload) == 0 :
        r= requests.get('http://localhost:5000/component')
    else :
        r= requests.get('http://localhost:5000/component',params=payload)
    # convert response to list
    # r.json() is {'Components': [{'id': 5, 'position': 8, 'weight': 3.75},...]}
    lcp = list(r.json().values())[0]
    # create plot data 
    plot['data'] = {}
    plotData = {}
    plotData["color"] = "#425cef"

    plotData["dataPoints"] = []
    for cp in lcp:
        plotData["dataPoints"].append({"x":cp['position'],"y":cp['weight']})
    # convert json to string
    plot['data'] = json.dumps(plotData)
    return plot

'''
*****************************
* API Resources Definition  *
*****************************
'''

api = Api(app)

api.add_resource(HelloWorldResource,'/hello')
api.add_resource(ComponentResource,'/component')
api.add_resource(MultiResource,'/multi/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)