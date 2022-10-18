from flask_wtf import FlaskForm
from wtforms import DateField,FloatField, SubmitField,TimeField,HiddenField,SelectField
from wtforms.validators import DataRequired,ValidationError,NumberRange

def validar_moneda(form,field):
    if field.data == form.moneda_from.data:
        raise ValidationError("Debes elegir diferentes tipos de moneda")

class MovementForm(FlaskForm):
    id = HiddenField()
    date = DateField("Fecha")
    hora = TimeField("Hora")

    moneda_from = SelectField("From",choices=[
        ("EUR", "EUR"), ("BTC", "BTC"), ("ETH", "ETH"), ("LUNA", "LUNA"), ("LINK", "LINK")], validators=[DataRequired()])
    moneda_to = SelectField("To", choices=[
        ("EUR", "EUR"), ("BTC", "BTC"), ("ETH", "ETH"), ("LUNA", "LUNA"), ("LINK", "LINK")], validators=[DataRequired(), validar_moneda])
    
 
    cantidad_from = FloatField("Q:  ",validators=[DataRequired(message="La cantidad debe de ser un número positivo y mayor que 0"),
    NumberRange(min=0.00001, max=99999999)])


    consultar = SubmitField("Calcular")

    borrar = SubmitField("X")
    aceptar = SubmitField("√")

    