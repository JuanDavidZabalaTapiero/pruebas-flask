from flask import Blueprint, render_template, flash
from app.services.alumnos_service import obtener_todos_alumnos

alumnos_bp = Blueprint("alumnos", __name__)

@alumnos_bp.route("/")
def home():
    """
    Muestra la tabla de todos los alumnos registrados.
    """
    alumnos = obtener_todos_alumnos()

    if alumnos is None:
        flash("Ocurrió un error al intentar consultar los alumnos", "error_alumnos_home")

    return render_template("alumnos/home.html", alumnos=alumnos)
