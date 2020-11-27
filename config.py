import os


class Config(object):
    SECRET_KEY = 'my_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/flask?charset=utf8&use_unicode=True'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\db_organizate\organizate.db'
<<<<<<< Updated upstream
    # MYSQL_USER = 'root'
    # MYSQL_PASSWORD = ''
    # MYSQL_DB = 'cursoflask'
=======
    SQLALCHEMY_BINDS = {
    'calendary': 'mysql+pymysql://root@localhost/flaskmysql',
}
>>>>>>> Stashed changes
