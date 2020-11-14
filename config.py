import os

class Config(object):
    SECRET_KEY = 'Llave_secreta'

class DevelopmentConfig(Config):
    DEBUG = True
