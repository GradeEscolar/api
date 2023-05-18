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

    def upsert(self, data):
        aula = Aula()
        aula.from_dict(data)
        self.repository.upsert(aula)

    def delete(self, id: int):
        self.repository.delete(id)
