from flask import Blueprint, render_template, flash
from app.services.alumnos_service import obtener_todos_alumnos, crear_alumno
from app.forms.alumnos import RegistroAlumnoForm
from flask_babel import _

alumnos_bp = Blueprint("alumnos", __name__)

@alumnos_bp.route("/")
def home():
    """
    Muestra la tabla de todos los alumnos registrados junto con un botón para registrar uno nuevo.
    """
    alumnos = obtener_todos_alumnos()

    if alumnos is None:
        flash(_("Ocurrió un error al intentar consultar los alumnos"), "error_alumnos_home")

    return render_template("alumnos/home.html", alumnos=alumnos)

@alumnos_bp.route("/registrar", methods=["GET", "POST"])
def registrar_alumno():
    """
    Muestra y valida el formulario para registrar un nuevo alumno en la base de datos.
    """
    form = RegistroAlumnoForm()

    if form.validate_on_submit():
        nombres = form.nombres.data
        apellidos = form.apellidos.data

        alumno = crear_alumno(nombres, apellidos)
        if alumno:
            flash("Alumno registrado correctamente", "success_alumnos_registrar_alumno")
        else:
            flash("Ocurrió un error al intentar registrar el alumno", "error_alumnos_registrar_alumno")

    return render_template("alumnos/registrar.html", form=form)