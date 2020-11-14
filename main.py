from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import url_for
from flask import redirect
from flask import flash

import forms

app = Flask(__name__)
app.secret_key = 'Llave_secreta'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request()
def before_request():
    pass

@app.after_request()
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

if __name__ == '__main__':
    app.run(debug=True, port=8000)
