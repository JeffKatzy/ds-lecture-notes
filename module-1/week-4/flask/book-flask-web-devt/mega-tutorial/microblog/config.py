import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
     SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'microblogapp.db')
     SQLALCHEMY_ECHO=True
     SQLALCHEMY_TRACK_MODIFICATIONS = False
