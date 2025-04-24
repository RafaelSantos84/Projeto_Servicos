from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email

class BorrachariaForm(FlaskForm):
    nome = StringField('Nome da Barracharia', validators=[DataRequired()])
    endereco = StringField('Endereco', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    horario = StringField('Horario de Funcionamento', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')