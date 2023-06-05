from grade_escolar.repositories import GradeRepository
from grade_escolar.models import Grade

class GradeService:
    
    def __init__(self):
        self.repository = GradeRepository()
        
    def read(self, id_usuario:int):
        grades = self.repository.read(id_usuario)
        return [grade.to_dict() for grade in grades]
    
    def update(self, id_usuario:int, data):
        grade = Grade()
        grade.from_dict(data)
        if self.repository.exists(id_usuario, grade.id):
            self.repository.update(grade)
            
            return True
        return False
        