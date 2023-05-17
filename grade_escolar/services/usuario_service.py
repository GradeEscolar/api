from datetime import datetime, timedelta
import bcrypt
from grade_escolar.repositories import UsuarioRepository
from grade_escolar.models import Usuario, Grade

class UsuarioService:
    
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def create(self, data):
        usuario = Usuario()
        usuario.from_dict(data)
        usuario.data_cadastro = datetime.utcnow() - timedelta(hours=3)
        usuario.senha = bcrypt.hashpw(str(usuario.senha).encode(), bcrypt.gensalt())
        
        grade = Grade()
        grade.aulas = 5
        grade.dias = '2;3;4;5;6'
        usuario._grade = grade
        
        return self.usuario_repository.create(usuario)
        
    def read(self):
        usuarios = self.usuario_repository.listar()
        data = [usuario.to_dict() for usuario in usuarios]
        return data