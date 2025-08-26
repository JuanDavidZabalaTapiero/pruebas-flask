import pytest
from app.models.alumnos import Alumno
from app.services.alumnos_service import obtener_todos_alumnos

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