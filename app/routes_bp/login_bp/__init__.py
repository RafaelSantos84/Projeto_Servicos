from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models import Usuario
from app.forms import LoginForm

login_bp = Blueprint('login', __name__, template_folder='templates')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and usuario.verificar_senha(form.senha.data):
            login_user(usuario)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('logued_area_bp.home'))
        else:
            flash('Email ou senha incorretos.', 'danger')
    return render_template('login.html', form=form)

@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da conta.', 'info')
    return redirect(url_for('login.login'))