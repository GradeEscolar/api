from grade_escolar.data_access.repositories.disciplina_repository import DisciplinaRepository
from grade_escolar.data_access.models import Disciplina

class DisciplinaService:
    
    def __init__(self):
        self.repository = DisciplinaRepository()

    def create(self, id_usuario:int, data):
        disciplina = Disciplina()
        disciplina.from_dict(data)
        disciplina.id_usuario = id_usuario
        return self.repository.create(disciplina)
        
    def read(self, id_usuario: int):
        disciplinas = self.repository.read(id_usuario)
        data = [disciplina.to_dict() for disciplina in disciplinas]
        return data