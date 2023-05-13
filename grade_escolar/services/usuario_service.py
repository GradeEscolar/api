from datetime import datetime
from flask import jsonify
from sqlalchemy.orm import Session
from grade_escolar.data_access.repositories.usuario_repository import UsuarioRepository
from grade_escolar.data_access.models import Usuario, dict_to_class

class UsuarioService:
    
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def create(self, data):
        usuario = Usuario()
        usuario.from_dict(data)
        usuario.set_data_cadastro()
        return self.usuario_repository.create(usuario)
        
    def read(self):
        usuarios = self.usuario_repository.listar()
        data = [usuario.to_dict() for usuario in usuarios]
        return data