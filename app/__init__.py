from flask import Flask

def create_app():
    app = Flask(__name__)

    # == BLUEPRINTS ==
    from .blueprints.alumnos import alumnos_bp
    app.register_blueprint(alumnos_bp)

    return app