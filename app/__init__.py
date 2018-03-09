# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import sqlalchemy

# Initialize the app
application = Flask(__name__)

# Load the views
#from app import views

# Load the config file
application.config.from_object(Config)

# config
#application.config.from_envvar('MSIA_SETTINGS', silent=True)

# Initialize the database
db = SQLAlchemy(application)
