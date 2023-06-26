from typing import Optional
from sqlalchemy.orm import Session, joinedload
from grade_escolar.data_access import engine
from grade_escolar.models import Grade, Aula

class GradeRepository:
    
    def read(self, id_usuario: int):
        with Session(engine) as session:
            return session.query(Grade).filter(Grade.id_usuario == id_usuario).all()
        
    def exists(self, id_usuario: int, id: int):
        with Session(engine) as session:
            query = session.query(Grade).filter(
                Grade.id_usuario == id_usuario, Grade.id == id
            )
            return True if session.query(query.exists()).scalar() else False

    def update(self, grade: Grade):
        with Session(engine) as session:
            d = session.get(Grade, grade.id)
            if d:      
                d.aulas = grade.aulas
                d.dias = grade.dias
                # aulas = [aula for aula in d._aulas if aula.aula > grade.aulas or grade.dias.find(str(aula.dia)) == -1]
                # for aula in aulas:
                #     session.delete(aula)
                    
                session.commit()