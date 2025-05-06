from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import Usuario
from app.forms import RegistroForm
from app import db

register_pb = Blueprint('register_pb', __name__)

@register_pb.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistroForm()
    if form.validate_on_submit():
        usuario = Usuario(
            nome=form.nome.data,
            email=form.email.data,
            tipo=form.tipo.data
        )
        usuario.set_senha(form.senha.data)
        db.session.add(usuario)
        db.session.commit()
        flash('Usuário criado com sucesso! Faça login.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)
