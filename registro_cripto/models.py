import sqlite3
from config import ORIGIN_DATA

#Está todas las funciones del copipaste pero falta filtrar y modificar

def filas_to_diccionario(filas, columnas):
    resultado = []
    for fila in filas:
        posicion_columna = 0
        d = {}
        for campo in columnas:
            d[campo[0]] = fila[posicion_columna]
            posicion_columna += 1
        resultado.append(d)

    return resultado
#Consulta de movimientos
def select_all():
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()

    cur.execute("SELECT id, date, time, quantity_from, coin_to, quantity_to from movements order by date;")

    resultado = filas_to_diccionario(cur.fetchall(), cur.description)

    conn.close()

    return resultado



def select_by(id):
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()

    cur.execute("SELECT id, date, concept, quantity from movements WHERE id = ?", (id,))

    resultado = filas_to_diccionario(cur.fetchall(), cur.description)
 
    conn.close()

    if resultado:
        return resultado[0]
    return {}






def insert(registro):
    """
    INSERT INTO movements (date, concept, quantity) values (?, ?, ?)

    params:     cur.execute("INSERT INTO movements (date, concept, quantity) values (?, ?, ?)", ['2022-04-08', 'Cumple', -80])

    conn.commit() antes de hacer el conn.close()
    """
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()

    cur.execute("INSERT INTO movements (date, concept, quantity) values (?, ?, ?);", registro)
    conn.commit()
    conn.close()

def delete_by(id):
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()

    cur.execute("DELETE FROM movements WHERE id = ?", (id,))

    conn.commit()
    conn.close()