from registro_cripto import app
from flask import render_template,request, redirect, url_for, flash
from registro_cripto.models import CriptoExchange,SqliteManager,APIError,consultaValorActual
from registro_cripto.forms import MovementForm
from datetime import date,datetime



RUTA = "data/movimientos.sqlite"

@app.route("/")
def index():
    try:
        sqlite = SqliteManager(RUTA)
        movimientos = sqlite.consultaSQL("SELECT * FROM movimientos ORDER BY date")
        return render_template("index.html",movements = movimientos, puntero = "index.html")
        
    except:
        flash("Base de datos no disponible,intentelo más tarde",
              category="fallo")
        return render_template("index.html")

     


@app.route("/purchase", methods=["GET", "POST"])
def mercado():

    if request.method == "GET":
        form = MovementForm()
        return render_template("purchase.html", form=form, puntero="purchase.html")
    else:
        try:
            form = MovementForm(data=request.form)

            moneda_from = form.moneda_from.data
            moneda_to = form.moneda_to.data
            cantidad_from = form.cantidad_from.data
            cantidad_from = float(round(cantidad_from, 8))

            convertir = CriptoExchange(moneda_from, moneda_to)
            PU = convertir.consultar_cambio()
            PU = float(round(PU, 8))
            cantidad_to = cantidad_from * PU
            cantidad_to = float(round(cantidad_to, 8))

            saldo = SqliteManager(RUTA).calcular_saldo(moneda_from)
            if moneda_from != "EUR" and saldo < float(cantidad_from):
                flash("No tienes suficientes monedas {} ".format(moneda_from))
                return render_template("purchase.html", form=form)
                
            if form.consultar.data:
                return render_template("purchase.html", form=form, cantidad_to=cantidad_to, PU=PU)

        except APIError as err:
            flash(err)
            return render_template("purchase.html", form=form)

        if form.aceptar.data:
            if form.validate():
                form = MovementForm(data=request.form)
                sqlite = SqliteManager(RUTA)
                consulta = "INSERT INTO movimientos (date, time, moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES (?,?,?,?,?,?)"
                moneda_from = str(form.moneda_from.data)
                moneda_to = str(form.moneda_to.data)
                cantidad_from = float(cantidad_from)
                form.fecha.data = date.today()
                fecha = form.fecha.data
                form.hora.data = datetime.today().strftime("%H:%M:%S")
                hora = form.hora.data
                params = (fecha, hora, moneda_from,
                          cantidad_from, moneda_to, cantidad_to)
                resultado = sqlite.consultaConParametros(consulta, params)

                if resultado:
                    flash("Movimiento actualizado correctamente", category="exito")
                    return redirect(url_for("index"))

                else:
                    return render_template("purchase.html", form=form, cantidad_to=cantidad_to, errores=["Ha fallado la conexión con las Base de datos"])

            else:
                return render_template("purchase.html", form=form, cantidad_to=cantidad_to, errores=["Ha fallado la validación de datos"])

        else:
            return redirect(url_for("mercado"))


@app.route("/status", methods=["GET"])
def estado():
    try:
        sqlite = SqliteManager(RUTA)
        euros_to = sqlite.consultar_saldo(
            "SELECT sum(cantidad_to) FROM movimientos WHERE moneda_to='EUR'")
        euros_to = euros_to[0]
        if euros_to == None:
            euros_to = 0
        euros_from = sqlite.consultar_saldo(
            "SELECT sum(cantidad_from) FROM movimientos WHERE moneda_from='EUR'")
        euros_from = euros_from[0]
        if euros_from == None:
            euros_from = 0
        saldo_euros_invertidos = euros_from - euros_to 
        saldo_euros_invertidos = round(saldo_euros_invertidos, 8)
        total_euros_invertidos = euros_from
        recuperado = euros_to

        cripto_from = sqlite.total_euros_invertidos(
            "SELECT moneda_from, sum(cantidad_from) FROM movimientos GROUP BY moneda_from")
        totales_from = []
       
        try:

            for valor_from in cripto_from:
                convertir = CriptoExchange(valor_from[0], "EUR")
                valor = convertir.consultar_cambio()
                valor = convertir.cambio
                valor = float(valor)
                valor = valor * valor_from[1]
                valor = totales_from.append(valor)
            suma_valor_from = sum(totales_from)

            cripto_to = sqlite.total_euros_invertidos(
                "SELECT moneda_to, sum(cantidad_to) FROM movimientos GROUP BY moneda_to")

            totales_to = []

            for valor_to in cripto_to:
                convertir = CriptoExchange(valor_to[0], "EUR")
                valor = convertir.consultar_cambio()
                valor = convertir.cambio
                valor = float(valor)
                valor = valor * valor_to[1]
                valor = totales_to.append(valor)
            suma_valor_to = sum(totales_to)
            
            
            inversion_atrapada = suma_valor_to - suma_valor_from
            valor_actual = consultaValorActual()
            valor_actual = round(valor_actual, 8)
            ganancia = round(valor_actual - saldo_euros_invertidos,2)
            

            return render_template("status.html", euros_to=euros_to, euros_from=euros_from, total_euros_invertidos=total_euros_invertidos,\
                saldo_euros_invertidos=saldo_euros_invertidos,recuperado=recuperado,inversion_atrapada=inversion_atrapada,valor_actual=valor_actual,ganancia=ganancia,puntero="status.html")
        except APIError:
            flash("Error en la consulta de STATUS con el servidor (API)",
            category="fallo")
            return render_template("status.html")
    except:
        flash("No hay movimientos en tu base de datos SQLITE, ahora mismo no podemos calcular",
            category="fallo")
        return render_template("status.html")


