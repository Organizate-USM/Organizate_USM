from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import datetime


db1 = SQLAlchemy()
db2 = SQLAlchemy()
class User(db1.Model):
    __tablename__ = 'users'

<<<<<<< Updated upstream
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(96))
    created_date = db.Column(db.DateTime, default= datetime.datetime.now)
=======
    id = db1.Column(db1.Integer, primary_key=True)
    username = db1.Column(db1.String(50), unique=True)
    email = db1.Column(db1.String(40))
    password = db1.Column(db1.String(96))
    created_date = db1.Column(db1.DateTime, default= datetime.datetime.now)
>>>>>>> Stashed changes

    def __repr__(self):
        return "<Equipo %r>" %self.username

    def  __init__(self, username,email,password):
        self.username = username
        self.password = self.__create_password(password)
        self.email = email

    def __create_password(self,password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return self.password
        return check_password_hash(self.password, password)

class Calendary(db2.Model):
    __bind_key__ = 'calendary'
    __tablename__ = 'calendary'
    id = db2.Column(db2.Integer, primary_key=True)
    fechas = db2.Column(db2.String(80), unique=True)
    horario = db1.Column(db1.String(50), unique=True)
    a = db1.Column(db1.String(40))

    def  __init__(self, fechas,horario,a):
        self.fechas = fechas
        self.horario = horario
        self.a = a