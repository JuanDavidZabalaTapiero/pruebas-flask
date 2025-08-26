from .alumnos import alumnos_bp

def regiser_blueprints(app):
    """
    Registra todos los blueprints importados
    """
    app.register_blueprint(alumnos_bp)