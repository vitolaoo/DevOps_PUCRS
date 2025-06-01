# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_object=None):
    app = Flask(__name__)
    # Configuração básica: banco SQLite em arquivo local "movies.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'mudar-esta-chave-para-uma-mais-segura'

    db.init_app(app)

    # Cria as tabelas, se ainda não existirem
    with app.app_context():
        db.create_all()

    # Importa e registra Blueprints ou rotas
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
