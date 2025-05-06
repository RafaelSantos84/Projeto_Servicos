from flask import Blueprint, render_template

from app.routes_bp.login_bp import login_bp
from app.routes_bp.logued_area_bp import logued_area_bp
from app.routes_bp.register_bp import register_bp

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

def register_blueprints(app):
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(logued_area_bp)

    app.register_blueprint(main)
