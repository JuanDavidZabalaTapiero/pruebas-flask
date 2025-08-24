from flask import Blueprint, render_template

alumnos_bp = Blueprint("alumnos", __name__)

@alumnos_bp.route("/")
def home():
    return render_template("home.html")
