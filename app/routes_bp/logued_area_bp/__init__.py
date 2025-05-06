from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import Servico
from app.forms import ServicoForm
from app import db

logued_area_bp = Blueprint('logued_area_bp', __name__)
@logued_area_bp.route('/home')
@login_required
def home():
    return render_template('borracharias.html')

@logued_area_bp.route('/cadastro', methods=['GET', 'POST'])
@login_required
def cadastro():
    form = ServicoForm()
    if form.validate_on_submit():
        novo_servico = Servico(
            nome=form.nome.data,
            tipo=form.tipo.data,  # <-- Salvar o tipo aqui também
            endereco=form.endereco.data,
            telefone=form.telefone.data,
            horario=form.horario.data,
            usuario_id=current_user.id
        )
        db.session.add(novo_servico)
        db.session.commit()
        flash('Serviço cadastrado com sucesso!', 'success')
        return redirect(url_for('main.home'))
    return render_template('cadastro.html', form=form)
