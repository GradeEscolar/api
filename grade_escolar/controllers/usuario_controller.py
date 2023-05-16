from flask import Blueprint, request, jsonify
from grade_escolar.services import UsuarioService

# encoding: utf-8

controller = Blueprint('usuario_controller', __name__, url_prefix='/usuario')
service = UsuarioService()

@controller.get('')
def get():
    return jsonify(service.read())

@controller.post('')
def post():
    data = request.get_json()
    status_code = 200
    result = {
        'success': True,
        'message': None
    }
    if not(service.create(data)):
        result['success'] = False
        result['message'] = 'O e-mail informado já está em uso.'
        status_code = 409
    
    response = jsonify(result)
    response.status_code = status_code
    return response