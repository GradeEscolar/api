from datetime import timedelta
import bcrypt
from flask_jwt_extended import create_access_token
from grade_escolar.data_access.repositories import UsuarioRepository
from grade_escolar.data_access.models import Usuario

class LoginService:

    def __init__(self):
        self.repository = UsuarioRepository()

    def create_access_token(self, data):
        usuario = Usuario()
        usuario.from_dict(data)
        usuario_db = self.repository.obter_login(usuario)
        if usuario_db == None or not bcrypt.checkpw(str(usuario.senha).encode(), str(usuario_db.senha).encode()):
            return None

        access_token = create_access_token(
            identity=usuario_db.id, expires_delta=timedelta(days=365))

        return access_token
