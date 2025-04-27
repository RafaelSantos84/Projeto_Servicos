from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email

class ServicoForm(FlaskForm):
    nome = StringField('Nome do Serviço', validators=[DataRequired()])
    
    tipo = SelectField('Tipo de Serviço', choices=[
        ('borracharia', 'Borracharia'),
        ('oficina_mecanica', 'Oficina Mecânica'),
        ('funilaria', 'Funilaria'),
        ('auto_elétrica', 'Auto Elétrica'),
        ('revisao', 'Revisão'),
        ('lavagem', 'Lavagem'),
        ('moto_oficina', 'Oficina de Motos'),
        ('moto_borracharia', 'Borracharia para Motos'),
        ('moto_revisao', 'Revisão de Motos'),
        ('moto_lavagem', 'Lavagem de Motos'),
        ('outro', 'Outro')
    ])
    
    endereco = StringField('Endereço', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    horario = StringField('Horário de Funcionamento', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class CadastroUsuarioForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    tipo = SelectField('Tipo de Conta', choices=[('borracharia', 'Borracharia'), ('admin', 'Admin')])
    submit = SubmitField('Cadastrar')
