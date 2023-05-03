from flask import Flask

app_server = Flask(__name__)

from app.controllers import home_blueprint, login_blueprint

blueprints = [
    home_blueprint,
    login_blueprint
]
        
for blueprint in blueprints:
    app_server.register_blueprint(blueprint)

def get_server():
    return app_server