from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from grade_escolar.services import LoginService

controller = Blueprint('grade_controller', __name__, url_prefix='/grade')

@controller.get('')
@jwt_required()
def get():
    id_usuario = get_jwt_identity()
    
