import os

class Config:
    SECRET_KEY = 'SECRET_KEY'
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'borracharias.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
