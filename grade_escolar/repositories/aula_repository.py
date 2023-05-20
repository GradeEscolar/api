from typing import List
from sqlalchemy.orm import Session
from grade_escolar.data_access import engine
from grade_escolar.models import Aula


class AulaRepository:

    def sinc(self, create: List[Aula], update: List[Aula], delete: List[Aula]):
        with Session(engine) as session:
            session.add_all(create)
            for aula in update:
                aula_db = session.get(Aula, aula.id)    
                aula_db.id_disciplina = aula.id_disciplina
            
            for aula in delete:
                aula_db = session.get(Aula, aula.id)
                session.delete(aula_db)
                
            session.commit()
            
    def read(self, aula: Aula):
        with Session(engine) as session:
            return session.query(Aula).filter(
                Aula.id_grade == aula.id_grade, Aula.dia == aula.dia
            ).all()

    def delete(self, id: int):
        with Session(engine) as session:
            aula = session.get(Aula, id)
            if aula:
                session.delete(aula)
                session.commit()
