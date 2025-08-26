from flask import Flask
import os
from .extensions import db
from dotenv import load_dotenv

def create_app():

    # CARGAR VAR ENV
    load_dotenv()

    app = Flask(__name__)

    # == CONFIG ==
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}"
        f"@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}"
    )
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # == INICIALIZAR EXTENSIONES ==
    db.init_app(app)

    # == BLUEPRINTS ==
    from .blueprints.alumnos import alumnos_bp
    app.register_blueprint(alumnos_bp)

    return app