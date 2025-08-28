import pytest
from app.models.alumnos import Alumno
from app.services.alumnos_service import obtener_todos_alumnos, crear_alumno

def test_obtener_todos_alumnos_devuelve_lista(session):
    """
    Verifica que obtener_todos_alumnos retorna todos los alumnos insertados.
    """
    alumno1 = Alumno(nombres="Juan", apellidos="Pérez")
    alumno2 = Alumno(nombres="Ana", apellidos="García")
    session.add_all([alumno1, alumno2])
    session.commit()

    resultado = obtener_todos_alumnos()

    assert resultado is not None
    assert len(resultado) == 2
    assert any(a.nombres == "Juan" for a in resultado)
    assert any(a.nombres == "Ana" for a in resultado)

def test_crear_alumno_inserta_en_bd(session):
    """
    Verifica que crear_alumno inserta un alumno en la base de datos
    y retorna la instancia creada.
    """
    alumno = crear_alumno("Juan", "Zabala")

    assert alumno is not None
    assert alumno.id is not None
    assert alumno.nombres == "Juan"
    assert alumno.apellidos == "Zabala"

    resultado = Alumno.query.filter_by(nombres="Juan").first()
    assert resultado is not None
    assert resultado.apellidos == "Zabala"

def test_crear_alumno_devuelve_none_si_error(session):
    """
    Verifica que crear_alumno retorna None si ocurre un error en la BD.
    """
    alumno = crear_alumno(None, "Ramírez")  # nombres es obligatorio
    assert alumno is None
