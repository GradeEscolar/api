from flask import Blueprint, request, jsonify
from grade_escolar.services import UsuarioService
from .controllers_util import create_response

# encoding: utf-8

controller = Blueprint('usuario_controller', __name__, url_prefix='/usuarios')
service = UsuarioService()

@controller.get('')
def get():
    return jsonify(service.read())

@controller.post('')
def post():
    data = request.get_json()
    return create_response() if service.create(data) else create_response(409, 'O e-mail informado já está em uso.')