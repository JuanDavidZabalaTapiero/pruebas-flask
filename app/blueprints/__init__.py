from .alumnos import alumnos_bp

def register_blueprints(app):
    """
    Registra todos los blueprints importados
    """
    app.register_blueprint(alumnos_bp)