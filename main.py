from flask import Flask, render_template, request, make_response
from flask import session, url_for, redirect, flash, g
# from models import db1, User, Todo, Event,config,db
from models import User, config, db
from flask_wtf import CsrfProtect
from flask_bootstrap import Bootstrap
from config import DevelopmentConfig

import forms

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
        usuarios = (db.child("Datos").get()).val()
        listaUsuarios = []
        for usuario in usuarios:
            listaUsuarios.append(usuarios[usuario])

        for lista in listaUsuarios:
            if username == lista["Usr"] and  User.verify_password(lista["psw"],password):
                success_message = 'Bienvenido {}'.format(username)
                flash(success_message)
                session['username'] = username
                return redirect(url_for('index'))

        # user = User.query.filter_by(username = username).first()
        # if user is not None and user.verify_password(password):
        #     success_message = 'Bienvenido {}'.format(username)
        #     flash(success_message)
        #     session['username'] = username
        #     return redirect(url_for('index'))
        else:
            error_message = ' Usuario o contraseña no válida '
            flash(error_message)

    return render_template('login.html', form = login_form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    register_form = forms.RegisterForm(request.form)
    print(register_form)
    if request.method == 'POST' and register_form.validate():

        username = register_form.username.data
        email = register_form.email.data

        # user_verify = User.query.filter_by(username = username).first()
        # print(user_verify)
        # user_verify = User.query.filter_by(email = email).first()
        # print(user_verify)
        
        unico = True
        usuarios = (db.child("Datos").get()).val()
        listaUsuarios = []
        for usuario in usuarios:
            listaUsuarios.append(usuarios[usuario])

        for lista in listaUsuarios:
            if username == lista["Usr"] or email == lista["email"]:
                unico = False

            
        # if user_verify is None:
        #     user = User(register_form.username.data,
        #                 register_form.email.data,
        #                 register_form.password.data)
            # db1.session.add(user)
            # db1.session.commit()
               
        if unico == True:
            usuarios = db.child("Datos").push({"Usr":register_form.username.data, "psw":User.create_password(register_form.password.data), "email":register_form.email.data})
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
    username = session['username']
    return render_template('material.html',username=username)

@app.route('/informatica')
def informatica():
    username = session['username']
    return render_template('informatica.html',username=username)

@app.route('/matematica')
def matematica():
    username = session['username']
    return render_template('matematica.html',username=username)

@app.route('/arqui')
def arqui():
    username = session['username']
    return render_template('arqui.html',username=username)

@app.route('/industrial')
def industrial():
    username = session['username']
    return render_template('industrial.html',username=username)

@app.route('/elo')
def elo():
    username = session['username']
    return render_template('elo.html',username=username)

@app.route('/minas')
def minas():
    username = session['username']
    return render_template('minas.html',username=username)

@app.route('/pomodoro')
def pomodoro():
    username = session['username']
    return render_template('pomodoro.html',username=username)

@app.route('/pomodoroD')
def pomodoroD():
    username = session['username']
    return render_template('pomodoroD.html',username=username)

@app.route('/todolist')
def todolist():
    return render_template('todolist.html')
    
@app.route('/calendary')
def calendary():

    username = session['username']
    eventos = db.child("user").child(username).child("calendary").get()
    dic = eventos.val()
    listaEventos = []

    if dic != None:
        for eventito in dic:
	        listaEventos.append(dic[eventito])

    return render_template('calendary.html', listaEventos = listaEventos)


if __name__ == '__main__':
    csrf.init_app(app)
    # db1.init_app(app)
    # with app.app_context():
    #     db1.create_all()
    app.run(port=8000)
