from datetime import datetime, timedelta
import bcrypt
from grade_escolar.data_access.repositories.usuario_repository import UsuarioRepository
from grade_escolar.data_access.models import Usuario

class UsuarioService:
    
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def create(self, data):
        usuario = Usuario()
        usuario.from_dict(data)
        usuario.data_cadastro = datetime.utcnow() - timedelta(hours=3)
        usuario.senha = bcrypt.hashpw(str(usuario.senha).encode(), bcrypt.gensalt())
        return self.usuario_repository.create(usuario)
        
    def read(self):
        usuarios = self.usuario_repository.listar()
        data = [usuario.to_dict() for usuario in usuarios]
        return data