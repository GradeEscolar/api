from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

controller = Blueprint('anotacao_controller', __name__, url_prefix='/anotacao')
