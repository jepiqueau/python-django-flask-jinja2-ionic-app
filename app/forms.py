from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError, NumberRange

from app import app

class MinMaxCheck(object):
    def __init__(self, min=-1, max=-1, message=None):
        self.min = min
        self.max = max
        if not message:
            message = u'Position must be between %i and %i' % (min, max)
        self.message = message

    def __call__(self, form, field):
        if len(field.data) > 0 :
            l = int(field.data) or 0
            if l < self.min or self.max != -1 and l > self.max:
                raise ValidationError(self.message)

def create_position_form(minval,maxval) :
    class PositionForm(FlaskForm):
        pass
    print('create_position_form ',minval,maxval)
    data=[ ('Choose','--Please choose a Position--'),('All','all'),('One','one'), ('From','from'),
                  ('To','to'), ('FromTo','from->to')]
    sel_option = SelectField('Position Selector', choices = data, validators = [DataRequired()])
    setattr(PositionForm,'sel_option',sel_option)
    sel_from = StringField('From',validators = [MinMaxCheck(min=minval,max=maxval)])
    setattr(PositionForm,'sel_from',sel_from)
    sel_to = StringField('To',validators = [MinMaxCheck(min=minval,max=maxval)])
    setattr(PositionForm,'sel_to',sel_to)
    submit = SubmitField('Plot')
    setattr(PositionForm,'submit',submit)
    return PositionForm()

