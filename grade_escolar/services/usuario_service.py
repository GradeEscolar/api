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
        usuario = usuarios[0]
        d = {}
        for k in vars(usuario).items():
            if k[0] != '_sa_instance_state':
                d[k[0]] = k[1]
                
        print(d)
                
        
        #data = [usuario.to_dict() for usuario in usuarios]
        return d