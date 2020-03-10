import json
from app import app, db
from app.models import Component, Maintenance
from datetime import datetime, timedelta

#read a components json file
with open('components_data.json','r') as cp:
    array = json.load(cp)

for cpt in array['components'] :
    c = Component(position=cpt['position'],weight=cpt['weight'])
    db.session.add(c)
db.session.commit()

#read a maintenances json file
with open('maintenances_data.json','r') as ms:
    array = json.load(ms)
index = 20
for mt in array['maintenances'] :
    d = datetime.today() - timedelta(days=index)
    m = Maintenance(body=mt['body'],date=d,component_id=mt['component_id'])
    db.session.add(m)
    index -= 2
db.session.commit()   