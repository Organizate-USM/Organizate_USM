import os


class Config(object):
    SECRET_KEY = 'my_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/flaskmysql'
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\db_organizate\organizate.db'
#     SQLALCHEMY_BINDS = {
#     'sqlite' : 'sqlite:///C:\db_organizate\organizate.db',
# }
