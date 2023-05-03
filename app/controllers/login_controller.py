from flask import Blueprint, jsonify
from sqlalchemy.orm import Session
from app.services.login_service import LoginService

# encoding: utf-8

blueprint = Blueprint('login_controller', __name__, url_prefix='/login')
login_service = LoginService()

@blueprint.route('/')
def get():
    return login_service.usuarios()