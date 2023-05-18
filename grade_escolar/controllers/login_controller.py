from flask import Blueprint, jsonify, request
from grade_escolar.services import LoginService

# encoding: utf-8

controller = Blueprint('login_controller', __name__, url_prefix='/login')
service = LoginService()

@controller.get('')
def get():
    data = request.get_json()
    
    status_code = 401
    result = {
        'success': False,
        'message': 'E-Mail ou Senha inválidos.'
    }
    
    access_token = service.create_access_token(data)
    if access_token:
        status_code = 200
        result = {'access_token': access_token}
        
    response = jsonify(result)
    response.status_code = status_code
    return response