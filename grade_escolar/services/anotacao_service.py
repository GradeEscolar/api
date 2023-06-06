from grade_escolar.controllers.controllers_util import create_response
from grade_escolar.repositories import AnotacaoRepository
from grade_escolar.models import Anotacao

class AnotacaoService:
    
    def __init__(self):
        self.repository = AnotacaoRepository()
        
    def upsert(self, data):
        anotacao = Anotacao()
        anotacao.from_dict(data)
        id_db = self.repository.upsert(anotacao)
        anotacao.id = id_db
        return anotacao.to_dict()
    
    def read(self, data):
        anotacao = Anotacao()
        anotacao.from_dict(data)
        modo = data['modo']
        if modo == 'grade':
            anotacoes = self.repository.read_grade(anotacao)
            return [anotacao.to_dict() for anotacao in anotacoes]
        else:
            anotacoes = self.repository.read_disciplina(anotacao)
            return [anotacao.to_dict() for anotacao in anotacoes]
    
    def delete(self, id:int):
        self.repository.delete(id)