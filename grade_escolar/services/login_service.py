from flask import jsonify
from sqlalchemy.orm import Session
from grade_escolar.data_access.repositories.usuario_repository import UsuarioRepository

class LoginService:
    
    def __init__(self):
        self.usuario_repository = UsuarioRepository()
        
    def usuarios(self):
        usuarios = self.usuario_repository.listar_sqlalchemy()
        return jsonify(usuarios)