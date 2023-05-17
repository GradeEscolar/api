from grade_escolar.repositories import DisciplinaRepository
from grade_escolar.models import Disciplina

class DisciplinaService:
    
    def __init__(self):
        self.repository = DisciplinaRepository()

    def create(self, id_usuario:int, data):
        disciplina = Disciplina()
        disciplina.from_dict(data)
        disciplina.id_usuario = id_usuario
        return None if self.repository.create(disciplina) else 'A disciplina informada já existe.'
        
    def read(self, id_usuario: int):
        disciplinas = self.repository.read(id_usuario)
        data = [disciplina.to_dict() for disciplina in disciplinas]
        return data
    
    def update(self, id_usuario:int, data):
        disciplina = Disciplina()
        disciplina.from_dict(data)
        disciplina.id_usuario = id_usuario
        
        if not(self.repository.exists_id(disciplina.id_usuario, disciplina.id)):
            return 'Disciplina não localizada.'
        
        if(self.repository.exists_disciplina(disciplina.id_usuario, disciplina.disciplina)):
            return 'A disciplina informada já existe.'
        
        self.repository.update(disciplina.id, disciplina.disciplina)
        return None
    
    def delete(self, id_usuario:int, id:int):
        disciplina = Disciplina()
        disciplina.id = id
        disciplina.id_usuario = id_usuario
        
        if not(self.repository.exists_id(disciplina.id_usuario, disciplina.id)):
            return 'Disciplina não localizada.'
        
        self.repository.delete(disciplina.id)
        return None
        