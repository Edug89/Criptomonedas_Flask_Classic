## myCRYPTO
Aplicación web con la que podrás simular el registro la compra/venta de Criptomonedas, registro de inversiones y ver el estado de nuestra inversión.

## Instalación 
Para un correcto funcionamiento de la app, sigue estos pasos:
* **1. Clonar el repositorio**:
```git clone https://github.com/Edug89/Criptomonedas_Flask_Classic.git``` 

* **2. Creación y activación de entorno virtual**:
Si es windows```python -m venv <nombre del entorno virtual>``` y si es mac/linux ```python3 -m venv <nombre del entorno virtual>```
# linux / macos
```.<nombre del entorno virtual>/bin/activate```
# windows 
```.<nombre del entorno virtual>\Scripts\activate```

* **3. Instalación carpeta requirements**:
```pip install -r requirements.txt```

* **4. Variables de entorno**:
     Renombrar los archivos ```.env_template```como ```.env``` y el ```config_template.py```como ```config.py```
     Definir las variables de entorno: ```FLASK_APP=main.py``` ```FLASK_DEBUG=True``` y luego seguir las indicaciones dentro de config.py

* **5. Obtener APIKey**:
	Visitar la página [CoinAPI](https://www.coinapi.io/) para conseguir tu 	APIkey(	[obtener gratis aquí](https://www.coinapi.io/pricing?apikey))

* **6. Creación de BBDD**:
Descargar gestor de BBDD sqlite en el siguiente enlace: [sqlitebrowser](https://sqlitebrowser.org/dl/)
Abrir el archivo ```data/movimientos.sqlite```en el programa y ejecutarlo. ```estructura de la base de datos en el fichero create.sql```

## Ejecutar aplicacion 
Escribir en la terminal ```flask run(En caso de que te de problemas el puerto 5000 que indique estar ocupado inicar con flask run -p 5001)```

## DUDAS:
Cualquier duda en el funcionamiento de la aplicación contactar con (edugproduce@gmail.com)
