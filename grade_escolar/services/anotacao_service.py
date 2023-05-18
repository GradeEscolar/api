from grade_escolar.repositories import AnotacaoRepository
from grade_escolar.models import Anotacao

class AnotacaoService:
    
    def __init__(self):
        self.repository = AnotacaoRepository()
