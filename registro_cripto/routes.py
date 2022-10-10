from registro_cripto import app



@app.route("/")
def index():
    return "Servidor Funcionando!!!"

