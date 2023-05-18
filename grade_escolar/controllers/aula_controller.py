from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

controller = Blueprint('aula_controller', __name__, url_prefix='/aula')