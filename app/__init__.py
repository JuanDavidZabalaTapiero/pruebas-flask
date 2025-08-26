from flask import Flask
from .extensions import db, migrate
from .config import Config
from .blueprints import register_blueprints

def create_app(config_class=Config):
    """
    Crea y configura la app de Flask.

    Returns: Flask: instancia de la aplicación.
    """

    app = Flask(__name__)

    # == CONFIG ==
    app.config.from_object(config_class)

    # == INICIALIZAR EXTENSIONES ==
    db.init_app(app)
    migrate.init_app(app, db)

    # == IMPORTAR MODELOS ==
    from app import models

    # == REGISTRAR BLUEPRINTS ==
    register_blueprints(app)

    return app