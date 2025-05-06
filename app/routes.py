from flask import Blueprint, render_template

from app.routes_bp import login_bp
from app.routes_bp import register_pb
from app.routes_bp import logued_area_pb

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

def register_routes(app):
    app.register_blueprint(login_bp)
    app.register_blueprint(register_pb)
    app.register_blueprint(logued_area_pb)

    app.register_blueprint(main)
