from flask_wtf import FlaskForm
from wtforms import DateField,StringField, FloatField, SubmitField,TimeField,HiddenField
from wtforms.validators import DataRequired,ValidationError

def validar_moneda(form,field):
    if field.data == form.moneda_from.data:
        raise ValidationError("Debes elegir diferentes tipos de moneda")

class MovementForm(FlaskForm):
    id = HiddenField()
    date = DateField("Fecha")
    time = TimeField("Hora")
    coin_from = StringField("From",choices=[
        ("EUR", "EUR"), ("BTC", "BTC"), ("ETH", "ETH"), ("LUNA", "LUNA"), ("LINK", "LINK")], validators=[DataRequired()])
    coin_to = StringField("To", choices=[
        ("EUR", "EUR"), ("BTC", "BTC"), ("ETH", "ETH"), ("LUNA", "LUNA"), ("LINK", "LINK")], validators=[DataRequired(), validar_moneda])
    
    quantity_to = FloatField("Cantidad_To",validators=[DataRequired()])
    quantity_from = FloatField("Q",validators=[DataRequired()])

    borrar = SubmitField("X")
    aceptar = SubmitField("√")

    