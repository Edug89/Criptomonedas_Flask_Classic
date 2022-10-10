from flask import Flask

app = Flask(__name__)

from registro_cripto.routes import *
