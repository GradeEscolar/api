import os
from flask import Flask
from flask_cors import CORS

os.environ['TZ'] = 'America/Sao_Paulo'

app_server = Flask(__name__)
CORS(app_server)

from grade_escolar.controllers import home_controller, usuario_controller

controllers = [
    home_controller,
    usuario_controller    
]
        
for controller in controllers:
    app_server.register_blueprint(controller)

def get_server():
    return app_server