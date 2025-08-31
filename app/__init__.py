from flask import Flask, request
from .extensions import db, migrate, babel
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

    # == REGISTRAR SELECTOR DE IDIOMA ==
    def get_locale():
        lang = request.args.get("lang")
        if lang in app.config.get('BABEL_SUPPORTED_LOCALES', []):
            return lang
        return request.accept_languages.best_match(app.config.get("BABEL_SUPPORTED_LOCALES", []))

    # == INICIALIZAR EXTENSIONES ==
    db.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app, locale_selector=get_locale)

    # == IMPORTAR MODELOS ==
    from app import models

    # == REGISTRAR BLUEPRINTS ==
    register_blueprints(app)

    return app