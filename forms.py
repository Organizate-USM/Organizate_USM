from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField
from wtforms import TextAreaField
from wtforms import PasswordField


from wtforms import validators

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')

def email_usm(form, field):
    if "@usm.cl" not in field.data and "@sansano.usm.cl" not in field.data:
        raise validators.ValidationError("Tiene que ser un correo de la UTFSM")

class CommentForm(Form):
	comment = TextAreaField('Comentario')
	honeypot = HiddenField('', [length_honeypot])

class LoginForm(Form):
	username = StringField('Username',
				[
				validators.Required(message = '¡El username es requerido!.'),
				validators.length(min=4, max=25, message='¡Ingrese un username valido!.'),
				],
				render_kw={"placeholder": "Ingrese Username","autocomplete": "off"})
	password = PasswordField('Password',
                [
                validators.Required(message='El password es requerido')
                ],
				render_kw={"placeholder": "Ingrese Contraseña"})

class RegisterForm(Form):
	username = StringField('Username',
				[
				validators.Required(message = '¡El username es requerido!.'),
				validators.length(min=4, max=25, message='¡Ingrese un username valido!.'),
				],
				render_kw={"placeholder": "Ingrese Username", "autocomplete": "off"})

	email = EmailField('Email',
				[
				validators.Required(message = '¡El Email es requerido!.'),
				validators.length(min=4, max=50, message='¡Ingrese un Email valido!.'),
                email_usm,
				],render_kw={"placeholder": "Ingrese correo electronico", "autocomplete": "off"})

	password = PasswordField('Password',
                [
                validators.Required(message='El password es requerido')
                ],
				render_kw={"placeholder": "Ingrese Contraseña"})
