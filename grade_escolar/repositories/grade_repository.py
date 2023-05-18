from sqlalchemy.orm import Session
from grade_escolar.data_access import engine
from grade_escolar.models import Grade

class GradeRepository:
    
    def read(self, id_usuario: int):
        with Session(engine) as session:
            return session.query(Grade).filter(Grade.id_usuario == id_usuario).first()
        
    def exists(self, id_usuario: int, id: int):
        with Session(engine) as session:
            query = session.query(Grade).filter(
                Grade.id_usuario == id_usuario, Grade.id == id
            )
            return True if session.query(query.exists()).scalar() else False

    def update(self, grade: Grade):
        with Session(engine) as session:
            d = session.get(Grade, grade.id)
            d.aulas = grade.aulas
            d.dias = grade.dias
            session.commit()