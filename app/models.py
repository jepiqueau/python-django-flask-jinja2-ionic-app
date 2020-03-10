from datetime import datetime
from app import db

class Component(db.Model):
    __tablename__ = 'components'
    id = db.Column(db.Integer, primary_key=True) 
    position = db.Column(db.Integer, index=True, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    maintenances = db.relationship('Maintenance', backref='components', lazy=True)
    def __repr__(self):
        return '<Component {}>'.format({"id":self.id,"position":self.position,"weight":self.weight})
    def json(self) :
        return {"id":self.id,"position":self.position,"weight":self.weight}

class Maintenance(db.Model):
    __tablename__ = 'maintenances'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    component_id = db.Column(db.Integer, db.ForeignKey('components.id'),
        nullable=False)
    def __repr__(self):
        return '<Maintenance {}>'.format({"body":self.body,"date":self.date,"component_id":self.component_id})
    def json(self) :
        return {"id":self.id,"body":self.body,"date":self.date,"component_id":self.component_id}
