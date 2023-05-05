import json
from flask import Blueprint, make_response, request, jsonify
from sqlalchemy.orm import Session
from grade_escolar.services import UsuarioService
from grade_escolar.data_access.models import Usuario, dict_to_class

# encoding: utf-8

controller = Blueprint('usuario_controller', __name__, url_prefix='/usuario')
service = UsuarioService()

@controller.get('/')
def get():
    return jsonify(service.read())

@controller.post("/")
def post():
    data = request.get_json()
    service.create(data)
    return jsonify(success=True)