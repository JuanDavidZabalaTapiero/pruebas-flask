import pytest
from app.models.alumnos import Alumno
from unittest.mock import patch

def test_home_sin_alumnos(client):
    response = client.get("/")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "No hay alumnos registrados" in html
    assert "Registrar Alumno" in html

def test_home_con_alumnos(client, session):
    alumno = Alumno(nombres="Juan", apellidos="Pérez")
    session.add(alumno)
    session.commit()

    response = client.get("/")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Juan" in html
    assert "Pérez" in html
    assert "Registrar Alumno" in html

def test_home_flash_error_when_query_fails(client):
    """
    Si obtener_todos_alumnos() devuelve None, debe mostrarse un mensaje de error.
    """
    with patch("app.blueprints.alumnos.obtener_todos_alumnos", return_value=None):
        response = client.get("/")

        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Ocurrió un error al intentar consultar los alumnos" in html