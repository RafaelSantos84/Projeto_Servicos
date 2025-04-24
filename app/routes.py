from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from .forms import  LoginForm
from .models import Usuario
from . import db

main = Blueprint('main', __name__)

# Rota de login
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and usuario.verificar_senha(form.senha.data):
            login_user(usuario)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('E-mail ou senha incorretos.', 'danger')
    return render_template('login.html', form=form)

# Rota protegida (painel do usuário)
@main.route('/dashboard')
@login_required
def dashboard():
    return f'Bem-vindo, {current_user.nome}! Aqui é seu painel.'

# Rota de logout
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('main.login'))
