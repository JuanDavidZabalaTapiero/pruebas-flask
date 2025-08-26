from flask import Flask
from .extensions import db, migrate
from .config import Config

def create_app():

    app = Flask(__name__)

    # == CONFIG ==
    app.config.from_object(Config)

    # == INICIALIZAR EXTENSIONES ==
    db.init_app(app)
    migrate.init_app(app, db)

    # == MODELOS ==
    from app import models

    # == BLUEPRINTS ==
    from .blueprints.alumnos import alumnos_bp
    app.register_blueprint(alumnos_bp)

    return app