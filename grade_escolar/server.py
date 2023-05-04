from flask import Flask
from flask_cors import CORS

app_server = Flask(__name__)
CORS(app_server)

from grade_escolar.controllers import home_blueprint, login_blueprint

blueprints = [
    home_blueprint,
    login_blueprint
]
        
for blueprint in blueprints:
    app_server.register_blueprint(blueprint)

def get_server():
    return app_server