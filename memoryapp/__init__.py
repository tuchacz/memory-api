from flask import Flask
from flask_cors import CORS

app = Flask(__name__)  # instancja clasy flask
cors = CORS(app, resources={r"/*": {"origins": "*"}})  # wszystkie ścieżki które są w aplikacje zmniejszona jest restrykcja
app.debug = True  # włącza aplikacje flask w trybie debugowania

import memoryapp.routes
