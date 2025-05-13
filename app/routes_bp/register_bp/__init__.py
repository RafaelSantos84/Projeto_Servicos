from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import Usuario
from app.forms import RegistroForm
from app import db

register_bp = Blueprint('register_bp', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
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
        return redirect(url_for('logued_area_bp.login'))
    return render_template('register.html', form=form)
