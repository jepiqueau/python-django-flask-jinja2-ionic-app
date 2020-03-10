from app import app, db
from app.models import Component, Maintenance

# delete components
components = Component.query.all()
for cp in components:
    db.session.delete(cp)

# delete maintenances
maintenances = Maintenance.query.all()
for mt in maintenances:
    db.session.delete(mt)    

db.session.commit()