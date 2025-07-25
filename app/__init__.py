from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///servicos.db'
   
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login' # VERIFICAR se está ok! rota usada se o usuário não estiver logado

    from .models import Usuario

    @login_manager.user_loader
    def load_user(user_id): #VVERIFICAR se está ok! verifica se o usuário está logado
        return Usuario.query.get(int(user_id))
    
    from app.routes import register_blueprints
    register_blueprints(app)

    
    return app
