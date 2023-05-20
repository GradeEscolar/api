from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from grade_escolar.controllers.controllers_util import create_response
from grade_escolar.services import GradeService

controller = Blueprint('grade_controller', __name__, url_prefix='/grade')
service = GradeService()

@controller.get('')
@jwt_required()
def get():
    id_usuario = get_jwt_identity()
    return jsonify(service.read(id_usuario))

@controller.patch('')
@jwt_required()
def patch():
    id_usuario = get_jwt_identity()
    data = request.get_json()
    return create_response() if service.update(id_usuario, data) else create_response(400, 'Grade não localizada.')
    
