from app import app, db
from app.models import Component, Maintenance

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Component': Component, 'Maintenance': Maintenance}