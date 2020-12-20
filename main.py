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
from models import User
from models import Todo
from models import Event
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
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
    event = Event.query.all()
    return render_template('index.html', title = title, incomplete=incomplete, complete=complete, event=event)
    #return render_template('index.html', title = title, incomplete=incomplete, complete=complete)

@app.route('/addevent', methods=['GET', 'POST'])
def addevent():
    dia = request.form['fecha']
    listad = dia.split('-')
    meses = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    mes = meses[int(listad[1])-1]
    fechadb = '{}/{}/{}'.format(mes, listad[2], listad[0])
    mesesSpanish = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    mesSpanish = mesesSpanish[int(listad[1])-1]
    fechaleer = '{} de {} del {}'.format(listad[2], mesSpanish, listad[0])
    event = Event(nombre=request.form['nombre'], fecha=fechadb, descripcion=request.form['descripcion'], fechaleer=fechaleer )
    db1.session.add(event)
    db1.session.commit()
    return redirect(url_for('index'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    todo = Todo(text=request.form['todoitem'], complete=False)
    db1.session.add(todo)
    db1.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db1.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<id>')
def incomplete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = False
    db1.session.commit()
    return redirect(url_for('index'))

@app.route('/deleteitem/<id>')
def deleteitem(id):
    eliminar = Todo.query.filter_by(id=int(id)).first()
    db1.session.delete(eliminar)
    db1.session.commit()
    return redirect(url_for('index'))

@app.route('/deleteevent/<id>')
def deleteevent(id):
    eliminar = Event.query.filter_by(id=int(id)).first()
    db1.session.delete(eliminar)
    db1.session.commit()
    return redirect(url_for('index'))

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

@app.route('/pomodoro')
def pomodoro():
    return render_template('pomodoro.html')

if __name__ == '__main__':
    csrf.init_app(app)
    db1.init_app(app)
    with app.app_context():
        db1.create_all()
    app.run(port=8000)
