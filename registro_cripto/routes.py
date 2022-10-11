from registro_cripto import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html", pageTitle="Movimientos")

@app.route("/purchase")
def purchase():
    return render_template("purchase.html", pageTitle="Compra")

@app.route("/status")
def status():
    return "En construcción"
   

