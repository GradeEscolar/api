from typing import List
from grade_escolar.repositories import AulaRepository
from grade_escolar.models import Aula


class AulaService:

    def __init__(self):
        self.repository = AulaRepository()

    def read(self, data):
        aula = Aula()
        aula.from_dict(data)
        aulas = self.repository.read(aula)
        return [aula.to_dict() for aula in aulas]
    
    def _criar_aula(self, data):
        aula = Aula()
        aula.from_dict(data)
        return aula
        
    def sinc(self, data):
        aulas = [self._criar_aula(aula) for aula in data]
        create = [aula for aula in aulas if aula.id == None and aula.id_disciplina != None]
        update = [aula for aula in aulas if aula.id != None and aula.id_disciplina != None]
        delete = [aula for aula in aulas if aula.id != None and aula.id_disciplina == None]
        
        self.repository.sinc(create, update, delete)

    def delete(self, id: int):
        self.repository.delete(id)
