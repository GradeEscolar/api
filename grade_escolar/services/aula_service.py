from grade_escolar.repositories import AulaRepository
from grade_escolar.models import Aulas

class AulaService:
    
    def __init__(self):
        self.repository = AulaRepository()