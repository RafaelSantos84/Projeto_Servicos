from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import Usuario, db
from app.forms import LoginForm

main = Blueprint('main', __name__)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and usuario.verificar_senha(form.senha.data):
            login_user(usuario)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Email ou senha incorretos.', 'danger')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da conta.', 'info')
    return redirect(url_for('main.login'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = CadastroUsuarioForm()
    if form.validate_on_submit():
        novo_usuario = Usuario(
            nome=form.nome.data,
            email=form.email.data,
            tipo=form.tipo.data
        )
        novo_usuario.set_senha(form.senha.data)  # Criptografa a senha
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for('main.login'))  # Manda pro login depois de cadastrar
    return render_template('register.html', form=form)
