from grade_escolar.controllers.controllers_util import create_response
from grade_escolar.repositories import AnotacaoRepository
from grade_escolar.models import Anotacao

class AnotacaoService:
    
    def __init__(self):
        self.repository = AnotacaoRepository()
        
    def upsert(self, data):
        anotacao = Anotacao()
        anotacao.from_dict(data)
        self.repository.upsert(anotacao)
        return create_response()
    
    def read(self, data):
        anotacao = Anotacao()
        anotacao.from_dict(data)
        modo = data['modo']
        if modo == 'grade':
            result = self.repository.read_grade(anotacao)
            return result.to_dict() if result else {}
        else:
            anotacoes = self.repository.read_disciplina(anotacao)
            return [anotacao.to_dict() for anotacao in anotacoes]
    
    def delete(self, id:int):
        self.repository.delete(id)