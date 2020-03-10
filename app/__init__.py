from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
blog = {'name': 'Jeep Python Flask RestFul App'}
minmax = []
header = {'label': 'Jeep Python Flask RestFul App'}
from app import routes, resources, models, forms