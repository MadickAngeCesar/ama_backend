import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///routine.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
