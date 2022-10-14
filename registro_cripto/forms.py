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

    borrar = SubmitField("X")
    aceptar = SubmitField("√")


#Falta hacer bien la clase y enlazar.

Coins=[('EUR', 'Euro (€)'), 
        ('BTC', 'Bitcoin (BTC)'), 
        ('ETH', 'Ethereum (ETH)'), 
        ('XRP', 'Ripple (XRP)'), 
        ('LTC', 'Litecoin (LTC)'),
        ('BCH', 'Bitcoin Cash (BCH)'), 
        ('BNB', 'Binance (BNB)'), 
        ('USDT', 'Tether (USDT)'), 
        ('EOS', 'EOS (EOS)'), 
        ('BCHSV', 'Bitcoin Cash SV (BCHSV)'), 
        ('XLM', 'Stellar Lumens (XLM)'), 
        ('ADA', 'Cardano (ADA)'), 
        ('TRX', 'Tronix (TRX)') 
]