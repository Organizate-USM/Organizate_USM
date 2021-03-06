from flask import Flask, render_template, request, make_response
from flask import session, url_for, redirect, flash, g
from models import db1, User, Todo, Event
from flask_wtf import CsrfProtect
from flask_bootstrap import Bootstrap
from config import DevelopmentConfig
from firebase import firebase
import forms
import pyrebase
from collections import OrderedDict

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'my_secret_key'
csrf = CsrfProtect(app)
app.config.from_object(DevelopmentConfig)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
	if 'username' not in session and request.endpoint in ['index', 'cookie', 'material', 'informatica','pomodoro']:
		return redirect(url_for('login'))
	elif 'username' in session and request.endpoint in ['login', 'register']:
		return redirect(url_for('index'))

@app.after_request
def after_request(response):
    return response

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
    title = 'Index'
    return render_template('index.html', title = title, username=username)
    #return render_template('index.html', title = title, incomplete=incomplete, complete=complete)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)

    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data
        user = User.query.filter_by(username = username).first()

        if user is not None and user.verify_password(password):
            success_message = 'Bienvenido {}'.format(username)
            flash(success_message)
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error_message = ' Usuario o contraseña no válida '
            flash(error_message)

    return render_template('login.html', form = login_form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    register_form = forms.RegisterForm(request.form)
    if request.method == 'POST' and register_form.validate():
        username = register_form.username.data
        email = register_form.email.data
        user_verify = User.query.filter_by(username = username).first()
        user_verify = User.query.filter_by(email = email).first()
        if user_verify is None:
            user = User(register_form.username.data,
                        register_form.email.data,
                        register_form.password.data)

            db1.session.add(user)
            db1.session.commit()
            success_message = 'Cuenta registrada exitosamente'
            flash(success_message)
            return redirect(url_for('login'))
        else:
            error_message = 'Este usuario ya está registrado'
            flash(error_message)

    return render_template('register.html', form = register_form)

@app.route('/cookie')
def cookie():
    response = make_response( render_template('cookie.html'))
    response.set_cookie('custome_cookie', 'Felipe')
    return response

@app.route('/logout')
def logout():
    if "username" in session:
        session.pop('username')
    return redirect(url_for('login'))

@app.route('/material')
def material():
    return render_template('material.html')

@app.route('/informatica')
def informatica():
    return render_template('informatica.html')

@app.route('/matematica')
def matematica():
    return render_template('matematica.html')

@app.route('/arqui')
def arqui():
    return render_template('arqui.html')

@app.route('/industrial')
def industrial():
    return render_template('industrial.html')

@app.route('/elo')
def elo():
    return render_template('elo.html')

@app.route('/minas')
def minas():
    return render_template('minas.html')

@app.route('/civil')
def civil():
    return render_template('civil.html')

@app.route('/ambiental')
def ambiental():
    return render_template('ambiental.html')

@app.route('/mecanica')
def mecanica():
    return render_template('mecanica.html')

@app.route('/pomodoro')
def pomodoro():
    return render_template('pomodoro.html')

@app.route('/pomodoroD')
def pomodoroD():
    return render_template('pomodoroD.html')

@app.route('/todolist')
def todolist():
    return render_template('todolist.html')
    
@app.route('/calendary')
def calendary():
    config = {
    "apiKey": "AIzaSyD7geC0GEHTf9vREokkJGRRkad5BETp5q0",
    "authDomain": "organizateusm.firebaseapp.com",
    "databaseURL": "https://organizateusm-default-rtdb.firebaseio.com",
    "projectId": "organizateusm",
    "storageBucket": "organizateusm.appspot.com",
    "messagingSenderId": "950537281109",
    "appId": "1:950537281109:web:86dd2cd4dead3496053edc"
    }

    username = session['username']
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    eventos = db.child("user").child(username).child("calendary").get()
    dic = eventos.val()
    listaEventos = []

    if dic != None:
        for eventito in dic:
	        listaEventos.append(dic[eventito])

    return render_template('calendary.html', listaEventos = listaEventos)


if __name__ == '__main__':
    csrf.init_app(app)
    db1.init_app(app)
    with app.app_context():
        db1.create_all()
    app.run(port=8000)
