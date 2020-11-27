from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import url_for
from flask import redirect
from flask import flash
from flask import g
from flask_wtf import CsrfProtect
from flask_bootstrap import Bootstrap

from config import DevelopmentConfig
from models import db1
from models import db2
from models import User
import forms

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
	if 'username' not in session and request.endpoint in ['index', 'cookie', 'material', 'collaborate']:
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
	return render_template('index.html', title = title)

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
            error_message = 'Usuario o contraseña no válida'
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

@app.route('/collaborate')
def collaborate():
    return render_template('collaborate.html')


if __name__ == '__main__':
    csrf.init_app(app)
    db1.init_app(app)
    with app.app_context():
        db1.create_all()
        db2.create_all(bind=['calendary'])
    app.run(port=8000)
