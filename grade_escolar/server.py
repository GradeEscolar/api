import os
from flask import Flask
from flask_cors import CORS
from configparser import ConfigParser
from flask_jwt_extended import JWTManager

os.environ['TZ'] = 'America/Sao_Paulo'

config = ConfigParser()
config.read('config.ini')
jwt_secret = config['jwt']['jwt_secret']

app_server = Flask(__name__)
CORS(app_server, headers='Content-Type')
app_server.config["JWT_SECRET_KEY"] = jwt_secret
jwt = JWTManager(app_server)

from grade_escolar.controllers import home_controller, usuario_controller, login_controller, grade_controller, disciplina_controller, anotacao_controller, aula_controller

controllers = [
    home_controller,
    usuario_controller,
    login_controller,
    grade_controller,
    disciplina_controller,
    anotacao_controller,
    aula_controller
]
        
for controller in controllers:
    app_server.register_blueprint(controller)

def get_server():
    return app_server