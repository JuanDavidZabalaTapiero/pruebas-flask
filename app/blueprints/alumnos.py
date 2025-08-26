from flask import Blueprint, render_template

alumnos_bp = Blueprint("alumnos", __name__)

@alumnos_bp.route("/")
def home():
    """
    Muestra la tabla de los alumnos
    """
    return render_template("alumnos/home.html")
