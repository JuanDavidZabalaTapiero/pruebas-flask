from app.extensions import db

class Alumno(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)