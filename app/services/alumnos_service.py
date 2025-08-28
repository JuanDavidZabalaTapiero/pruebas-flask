from app.extensions import db
from app.models import Alumno
from sqlalchemy.exc import SQLAlchemyError

def obtener_todos_alumnos():
    """
    Returns: list[Alumno] | None: Lista de alumnos o None si ocurre un error.
    """
    try:
        return Alumno.query.all()
    
    except SQLAlchemyError as e:
        # ERROR EN CONSOLA
        print(f"Error al consultar los alumnos: {e}")
        db.session.rollback()
        return None
    
def crear_alumno(nombres: str, apellidos: str) -> Alumno | None:
    """
    Crea un nuevo alumno en la base de datos.
    Returns: Alumno creado o None si ocurre un error.
    """
    try:
        nuevo_alumno = Alumno(nombres=nombres, apellidos=apellidos)
        db.session.add(nuevo_alumno)
        db.session.commit()
        return nuevo_alumno
    except SQLAlchemyError as e:
        print(f"Error al intentar crear el alumno: {e}")
        db.session.rollback()
        return None