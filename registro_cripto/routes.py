from registro_cripto import app
from flask import render_template,request, redirect, url_for, flash
from registro_cripto.models import CriptoModel,SqliteManager,APIError
from registro_cripto.forms import MovementForm
from datetime import date,datetime

RUTA = "data/movimientos.sqlite"

@app.route("/")
def index():
    try:
        sqlite = SqliteManager(RUTA)
        movimientos = sqlite.consultaSQL("SELECT * FROM movimientos ORDER BY date")
        return render_template("index.html",movements = movimientos)
    except:
        flash("Base de datos no disponible,intentelo más tarde",
              category="fallo")
        return render_template("index.html")


@app.route("/purchase", methods=["GET", "POST"])
def compra():

    if request.method == "GET":
        form = MovementForm()
        return render_template("purchase.html", form=form)
    else:
        try:
            form = MovementForm(data=request.form)

            moneda_from = form.moneda_from.data
            moneda_to = form.moneda_to.data
            cantidad_from = form.cantidad_from.data
            cantidad_from = float(round(cantidad_from, 8))

            convertir = CriptoModel(moneda_from, moneda_to)
            PU = convertir.consultar_cambio()
            PU = float(round(PU, 8))
            cantidad_to = cantidad_from * PU
            cantidad_to = float(round(cantidad_to, 8))

            
            if form.consultar.data:
                return render_template("purchase.html", form=form, cantidad_to=cantidad_to, PU=PU)

        except APIError as err:
            flash(err)
            return render_template("purchase.html", form=form)

        if form.aceptar.data:
            if form.validate():
                form = MovementForm(data=request.form)
                db = SqliteManager(RUTA)
                consulta = "INSERT INTO movimientos (date, time, moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES (?,?,?,?,?,?)"
                moneda_from = str(form.moneda_from.data)
                moneda_to = str(form.moneda_to.data)
                cantidad_from = float(cantidad_from)
                form.date.data = date.today()
                fecha = form.date.data
                form.hora.data = datetime.today().strftime("%H:%M:%S")
                hora = form.hora.data
                params = (fecha, hora, moneda_from,
                          cantidad_from, moneda_to, cantidad_to)
                resultado = db.consultaConParametros(consulta, params)

                if resultado:
                    flash("Movimiento actualizado correctamente", category="exito")
                    return redirect(url_for("index"))

                else:
                    return render_template("purchase.html", form=form, cantidad_to=cantidad_to, errores=["Ha fallado la conexión con las Base de datos"])

            else:
                return render_template("purchase.html", form=form, cantidad_to=cantidad_to, errores=["Ha fallado la validación de datos"])

        else:
            return redirect(url_for("compra"))


@app.route("/status")
def status():
    return render_template("status.html")


