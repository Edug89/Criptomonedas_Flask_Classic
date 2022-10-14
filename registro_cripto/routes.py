from registro_cripto import app
from flask import render_template,request, redirect, url_for, flash
from registro_cripto.models import select_all,insert,select_by,delete_by
from registro_cripto.forms import MovementForm
from datetime import date


@app.route("/")
def index():
    try:
        movimientos = select_all("SELECT * FROM movimientos ORDER BY date")
        return render_template("inicio.html",pageTitle = "Índice", movs=movimientos)
    except:
        flash("No hay movimientos por el momento.",
              category="fallo")
        return render_template("index.html")



@app.route("/purchase", methods =["GET","POST"])
def purchase():
    if request.method == "GET":        
        compra_de_criptos = MovementForm()        
        return render_template("purchase.html", pageTitle = "Status", form=compra_de_criptos)    
    else:
        pass




@app.route("/status")
def status():
    return render_template("status.html")


 #Pruebas de funciones comparativas para añadir.
 
'''
def validaFormulario(camposFormulario):
    errores = []
    hoy = date.today().isoformat()
    if camposFormulario['date'] > hoy:
        errores.append("La fecha introducida es el futuro.")

    if camposFormulario['concept'] == "":
        errores.append("Introduce un concepto para la transacción.")

    #La primera condición es para que el número sea distinto de cero
    #la segunda condición es para que el campo no esté vacío
    if camposFormulario["quantity"] == "" or float(camposFormulario["quantity"]) == 0.0:
        errores.append("Introduce una cantidad positiva o negativa.")

    return errores
'''

'''
app.route("/purchase", methods=["GET", "POST"])
def purchase():
    form = MovementForm()
    if request.method == "GET":
        return render_template("purchase.html", el_formulario=form, pageTitle="Compra")
    else:
        if form.validate():
            insert([form.date.data.isoformat(),
                    form.time.data,
                    form.coin_from.data,
                    form.quantity_from.data,
                    form.coin_to.data,
                    form.quantity_to.data
                  ])
            return redirect(url_for("index"))
        else:
            return render_template("purchase.html", el_formulario=form)
'''
    

