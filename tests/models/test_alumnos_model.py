from app.models.alumnos import Alumno

def test_crear_y_consultar_alumno(session):
    """
    Verifica que un Alumno puede crearse y luego consultarse en la base de datos.
    """
    alumno = Alumno(nombres="Juan", apellidos="Pérez")
    session.add(alumno)
    session.commit()

    result = Alumno.query.filter_by(nombres="Juan").first()
    assert result is not None
    assert result.apellidos == "Pérez"