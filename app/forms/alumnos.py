from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class RegistroAlumnoForm(FlaskForm):
    nombres = StringField("Nombres", validators=[DataRequired(), Length(min=2, max=100)])
    apellidos = StringField("Apellidos", validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField("Registrar")