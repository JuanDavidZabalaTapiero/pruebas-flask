from flask import Flask
from .extensions import db, migrate
from .config import Config
from .blueprints import regiser_blueprints

def create_app():
    """
    Crea y configura la app de Flask.

    Returns: Flask: instancia de la aplicación.
    """

    app = Flask(__name__)

    # == CONFIG ==
    app.config.from_object(Config)

    # == INICIALIZAR EXTENSIONES ==
    db.init_app(app)
    migrate.init_app(app, db)

    # == IMPORTAR MODELOS ==
    from app import models

    # == REGISTRAR BLUEPRINTS ==
    regiser_blueprints(app)

    return app