# config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'application.db')
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flasktest:Desktop01@animaloutcomes.c76qrkgxophn.us-east-1.rds.amazonaws.com/animaloutcomes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Enable Flask's debugging features. Should be False in production
#DEBUG = True

#SECRET_KEY = 'development_key'
#SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/tracks.db'
#SQLALCHEMY_TRACK_MODIFICATIONS = False
