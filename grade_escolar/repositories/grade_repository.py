from sqlalchemy.orm import Session
from grade_escolar.data_access import engine
from grade_escolar.models import Grade

class GradeRepository:
    
    def read(self, id_usuario: int):
        with Session(engine) as session:
            return session.query(Grade).filter(Grade.id_usuario == id_usuario).first()
        
    def exists_id(self, id_usuario: int, id: int):
        with Session(engine) as session:
            query = session.query(Grade).filter(
                Grade.id_usuario == id_usuario, Grade.id == id
            )
            return session.query(query.exists()).scalar()

    def update(self, id: int, grade: Grade):
        with Session(engine) as session:
            d = session.get(Grade, id)
            d.aulas = grade.aulas
            d.dias = grade.dias
            session.commit()