from datetime import datetime
from flask import jsonify
from sqlalchemy.orm import Session
from grade_escolar.data_access.repositories.usuario_repository import UsuarioRepository
from grade_escolar.data_access.models import Usuario, dict_to_class

class UsuarioService:
    
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def create(self, data):
        usuario = dict_to_class(Usuario(), data)
        usuario.data_cadastro = datetime.now()
        self.usuario_repository.create(usuario)
        
    def read(self):
        return self.usuario_repository.listar()