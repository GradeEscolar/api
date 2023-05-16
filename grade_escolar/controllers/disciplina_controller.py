from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from grade_escolar.services import DisciplinaService

controller = Blueprint('disciplina_controller', __name__, url_prefix='/disciplina')

_service = DisciplinaService()

@controller.get('')
@jwt_required()
def get():
    id_usuario = get_jwt_identity()
    return jsonify(_service.read(id_usuario))

@controller.post('')
@jwt_required()
def post():
    id_usuario = get_jwt_identity()
    data = request.get_json()
    
    status_code = 200
    result = {
        'success': True,
        'message': None
    }
    
    if not(_service.create(id_usuario, data)):
        result['success'] = False
        result['message'] = 'A disciplina informada já existe.'
        status_code = 409
    
    response = jsonify(result)
    response.status_code = status_code
    return response