# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

# Initialize the app
application = Flask(__name__)

# Load the config file
application.config.from_object('config')

# Initialize the database
db = SQLAlchemy(application)
