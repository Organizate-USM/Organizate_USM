from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import url_for
from flask import redirect
from flask import flash
from flask import g

from config import DevelopmentConfig
from models import db
from models import User
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
	if 'username' not in session and request.endpoint in ['cookie']:
		return redirect(url_for('login'))
	elif 'username' in session and request.endpoint in ['login', 'create']:
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
        success_message = 'Bienvenido {}'.format(username)
        flash(success_message)
        session['username'] = login_form.username.data
    return render_template('login.html', form = login_form)

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
    db.init_app(app)
    app.run(port=8000)
    with app.app_context():
        db.create_all
