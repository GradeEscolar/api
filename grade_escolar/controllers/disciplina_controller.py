from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from grade_escolar.services import DisciplinaService
from .controllers_util import create_response

controller = Blueprint('disciplina_controller', __name__, url_prefix='/disciplinas')

service = DisciplinaService()

@controller.post('')
@jwt_required()
def post():
    id_usuario = get_jwt_identity()
    data = request.get_json()
    
    message = service.create(id_usuario, data)
    return create_response() if not(message) else create_response(400, message)

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
    
    message = service.update(id_usuario, data)
    return create_response() if not(message) else create_response(400, message)
    
@controller.delete('<int:id>')
@jwt_required()
def delete(id:int):
    id_usuario = get_jwt_identity()
    
    message = service.delete(id_usuario, id)
    return create_response() if not(message) else create_response(400, message)