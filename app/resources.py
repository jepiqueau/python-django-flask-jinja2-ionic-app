from flask import request, jsonify
from flask_restful import Resource
from sqlalchemy import and_, func
from app import db
from app.models import Component, Maintenance

import collections



class HelloWorldResource(Resource):
    def get(self):
            return {'about':'Hello World!'}
    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}, 201

class MultiResource(Resource):
    def get(self,num):
        return {'result':num * 10}

class ComponentResource(Resource):
        def get(self):
            args = request.args
            print('args ',args)
            if len(args) == 0 :
                components = Component.query.all()               
                return getResponse('Components',components), 201
            elif len(args) == 1 :
                if 'id' in args :
                    component = Component.query.filter_by(id=int(args['id'])).first()
                    return getResponse('Component',component), 201
                elif 'position' in args :
                    if args['position'] == 'minmax' :
                        values = db.session.query(func.min(Component.position),func.max(Component.position)).first()
                        return {'Components':{'min':values[0],'max':values[1]}}, 201
                    else :
                        component = Component.query.filter_by(position=int(args['position'])).first()
                        return getResponse('Component',component), 201
                elif 'range' in args :
                    components = db.session.query(Component.id,Component.position).all()             
                    return {'Components':components}, 201
                else :
                    return {'message':'Error argument must be either "id" or "position"'} , 400

            else :
                if 'filter' in args :
                    if args['filter'] == 'id' :
                        if 'from' in args and 'to' in args :
                            components = Component.query.filter(and_(Component.id <= int(args['to']), Component.id >= int(args['from'])))
                            return getResponse('Components',components), 201
                        elif 'from' in args :
                            components = Component.query.filter(Component.id >= int(args['from']))
                            return getResponse('Components',components), 201
                        elif 'to' in args :
                            components = Component.query.filter(Component.id <= int(args['to']))
                            return getResponse('Components',components), 201
                        else :
                            components = Component.query.all()               
                            return getResponse('Components',components), 201
                    elif args['filter'] == 'position' :
                        if 'from' in args and 'to' in args  :
                            components = Component.query.filter(and_(Component.position <= int(args['to']), Component.position >= int(args['from'])))
                            return getResponse('Components',components), 201
                        elif 'from' in args :
                            components = Component.query.filter(Component.position >= int(args['from']))
                            return getResponse('Components',components), 201
                        elif 'to' in args :
                            components = Component.query.filter(Component.position <= int(args['to']))
                            return getResponse('Components',components), 201
                        else :
                            components = Component.query.all()               
                            return getResponse('Components',components), 201
                    else :
                        return {'message':'Error "filter" must be "id" or "position"'} , 400
                else :
                    return {'message':'Error for more tha one argument "filter" must exist'} , 400
            
def getResponse(name,res) :
    print('res ',res)
    rlist = []
    if isinstance(res,collections.Iterable):        
        for r in res:
            rlist.append(r.json())
    else :
            rlist.append(res.json())
    rdict={}
    rdict[name] = rlist
    return rdict
