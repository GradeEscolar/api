from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from grade_escolar.controllers.controllers_util import create_response
from grade_escolar.services import AulaService

controller = Blueprint('aula_controller', __name__, url_prefix='/aula')

service = AulaService()


@controller.post('')
@jwt_required()
def post():
    data = request.get_json()
    return jsonify(service.read(data))


@controller.put('')
@jwt_required()
def put():
    data = request.get_json()
    service.upsert(data)
    return create_response()


@controller.delete('<int:id>')
@jwt_required()
def delete(id: int):
    service.delete(id)
    return create_response()
