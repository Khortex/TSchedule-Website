from dataclasses import field
from flask.templating import render_template
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import fields
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, Field, TextAreaField, widgets, SelectFieldBase
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired
from wtforms.widgets.core import SubmitInput

class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    remember_me = BooleanField("Recordar registro")
    submit = SubmitField("Acessar")

class CadastroForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField("Submeter")   

class PostagemForm(FlaskForm):
    #imagem = FileField(object)
    body = TextAreaField("Digite aqui a sua mensagem!", validators=[DataRequired()])
    submit = SubmitField("Envie Sua Postagem")
