
## myCRYPTO
Aplicación web con la que podrás simular el registro la compra/venta de Criptomonedas, registro de inversiones y ver el estado de nuestra inversión

## Instalación 
Para un correcto funcionamiento de la app, sigue estos pasos:
* **1. Clonar el repositorio**:
```git clone ```
* **2. Creación y activación de entorno virtual**:
```python -m venv <nombre del entorno virtual>```
# linux / macos
```source ./<nombre del entorno virtual>/bin/activate```
# windows 
```.\<nombre del entorno virtual>\Scripts\activate```
* **3. Instalación del entorno virtual**:
```pip install -r requirements.txt```
* **4. Variables de entorno**:
     Renombrar el archivo ```.env_template```como ```.env```
     Definir las variables de entorno: ```FLASK_APP=main.py```
     ```FLASK_ENV=development```
* **5. Obtener APIKey**:
	Visitar la página [CoinAPI](https://www.coinapi.io/) para conseguir tu 	APIkey(	[obtener gratis aquí](https://www.coinapi.io/pricing?apikey))
* **6. Creación de BBDD**:
Descargar gestor de BBDD sqlite en el siguiente enlace: [sqlitebrowser](https://sqlitebrowser.org/dl/)
Abrir el archivo ```registro_cripto/data/movimientos.sqlite```en el programa y ejecutarlo.
## Ejecutar aplicacion 
Escribir en la terminal ```flask run (En caso de que te de problemas el puerto que este ocupado inicar con flask run -p 5001)```
