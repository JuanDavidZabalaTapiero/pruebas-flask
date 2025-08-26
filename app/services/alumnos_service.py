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