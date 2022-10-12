from flask_wtf import FlaskForm
from wtforms import DateField,StringField, FloatField, SubmitField,TimeField
from wtforms.validators import DataRequired, Length

class MovementForm(FlaskForm):
    date = DateField("Fecha",validators =[DataRequired()])
    concept = StringField("Concepto",validators = [DataRequired(), Length(min=4, message="Mas de 4 caracteres,por favor")])
    quantity = FloatField("cantidad",validators = [DataRequired()])

    submit = SubmitField("Aceptar")

#Falta hacer bien la clase y enlazar.