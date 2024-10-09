import os

class Config:
    DEBUG = True
    SECRET_KEY = "some secret key which is not strong"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db.sqlite')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = 5001