import sqlite3
import requests
from config import API_KEY,ORIGIN_DATA


class SqliteManager:
    def __init__(self, ruta):
        self.ruta = ruta

    def consultaSQL(self, consulta):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta)

        self.movimientos = []
        nombres_columnas = []

        for desc_columna in cursor.description:
            nombres_columnas.append(desc_columna[0])

        datos = cursor.fetchall()
        for dato in datos:
            movimiento = {}
            indice = 0
            for nombre in nombres_columnas:
                movimiento[nombre] = dato[indice]
                indice += 1
            self.movimientos.append(movimiento)
        conexion.close()

        return self.movimientos

    def consultaConParametros(self, consulta, params):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        resultado = False
        try:
            cursor.execute(consulta, params)
            conexion.commit()
            resultado = True
        except Exception as error:
            print("ERROR SQLITE:", error)
            conexion.rollback()
        conexion.close()

        return resultado

    def consultar_saldo(self, consulta):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta)
        datos = cursor.fetchone()
        conexion.commit()
        conexion.close()
        return datos

    def total_euros_invertidos(self, consulta):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta)
        datos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        return datos

    def calcular_saldo(self, monedas):
        consulta_compras = "SELECT sum(cantidad_to) FROM movimientos WHERE moneda_to = '" + \
            monedas + "'"
        consulta_ventas = "SELECT sum(cantidad_from) FROM movimientos WHERE moneda_from = '" + \
            monedas + "'"

        datos_compras = self.consultar_saldo(consulta_compras)
        datos_ventas = self.consultar_saldo(consulta_ventas)
        if datos_ventas[0] == None and datos_compras[0] == None:
            return 0
        elif datos_ventas[0] == None:
            return datos_compras[0]
        elif datos_compras[0] == None:
            return 0
        else:
            return datos_compras[0] - datos_ventas[0]

class APIError(Exception):
    def __init__(self, code):
        if code == 400:
            msg = "Algo ha fallado en la consulta, vuelva a intentarlo más tarde."
        elif code == 401:
            msg = "Sin autorización -- Revise si su API KEY es correcta."
        elif code == 403:
            msg = "No tienes suficientes privilegios para realizar la consulta."
        elif code == 429:
            msg = "Has excedido el número de consultas para tu API KEY. Póngase en contacto en www.coinapi.io."
        elif code == 550:
            msg = "No hay información para la consulta realizada.Revise la configuración e inténtelo más tarde."
        else:
            msg = "Ha ocurrido un error. Por favor revise su conexión a Internet e inténtelo de nuevo mas tarde."
        super().__init__(msg)

class CriptoExchange:
    def __init__(self, origen, destino):
        self.moneda_origen = origen
        self.moneda_destino = destino
        self.cambio = 0.0

    def consultar_cambio(self):
        cabeceras = {
            "X-CoinAPI-Key": API_KEY
        }
        url = f"http://rest.coinapi.io/v1/exchangerate/{self.moneda_origen}/{self.moneda_destino}"
        respuesta = requests.get(url, headers=cabeceras)

        if respuesta.status_code == 200:
            self.cambio = respuesta.json()["rate"]
            return(self.cambio)

        else:
            raise APIError(respuesta.status_code)
    

def consultaSaldoCripto(crypto):
    cryptosMonedas = {}
    conn= sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()
    for moneda in crypto:
        consulta = f"SELECT ((SELECT (case when (SUM(cantidad_to)) is null then 0 else SUM(cantidad_to) end) as tot FROM movimientos WHERE moneda_to = '{moneda}') - (SELECT (case when (SUM(cantidad_from)) is null then 0 else SUM(cantidad_from) end) as ee FROM movimientos WHERE moneda_from = '{moneda}')) AS {moneda}"
        cur.execute(consulta)
        fila =cur.fetchall() 
        cryptosMonedas[moneda] = fila[0][0]  
    conn.close()
    
    return cryptosMonedas


def consultaValorActual():    
    total = 0
    monedas_disponibles = ["BTC", "EUR", "ETH", "XRP", "SOL","BNB","ADA","DOT","USDT","MATIC"]
    monederoActual = consultaSaldoCripto(monedas_disponibles)
    url = requests.get(f"https://rest.coinapi.io/v1/exchangerate/EUR?&apikey={API_KEY}")
    
    if url.status_code != 200:
        raise APIError(url.status_code)
    
    resultado = url.json()

    for a in monederoActual.keys():
        for b in resultado['rates']:
            if b['asset_id_quote'] == a:
                total += 1/b['rate'] * monederoActual[a]
                
    return total


