from flask_wtf import FlaskForm
from wtforms import DateField,StringField, FloatField, SubmitField,TimeField
from wtforms.validators import DataRequired, Length

class MovementForm(FlaskForm):
    date = DateField("Fecha",validators=[DataRequired()])
    time = TimeField("Hora",validators=[DataRequired()])
    coin_from = StringField("From",validators=[DataRequired()])
    quantity_from = FloatField("Q",validators=[DataRequired()])
    coin_to = StringField("To",validators=[DataRequired()])
    quantity_to = FloatField("Cantidad_To",validators=[DataRequired()])


#Falta hacer bien la clase y enlazar.