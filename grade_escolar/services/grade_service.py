from grade_escolar.repositories import GradeRepository
from grade_escolar.models import Grade

class GradeService:
    
    def __init__(self):
        self.repository = GradeRepository()