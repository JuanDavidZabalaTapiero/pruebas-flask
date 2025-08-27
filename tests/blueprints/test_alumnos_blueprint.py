import pytest
from app.models.alumnos import Alumno

def test_home_sin_alumnos(client):
    response = client.get("/")
    html = response.data.decode()
    assert response.status_code == 200
    assert "No hay alumnos registrados" in html
    assert "REGISTRAR" in html

def test_home_con_alumnos(client, session):
    alumno = Alumno(nombres="Juan", apellidos="Pérez")
    session.add(alumno)
    session.commit()

    response = client.get("/")
    html = response.data.decode()
    assert response.status_code == 200
    assert "Juan" in html
    assert "Pérez" in html
    assert "REGISTRAR" in html