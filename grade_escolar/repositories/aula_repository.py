from sqlalchemy.orm import Session
from grade_escolar.data_access import engine
from grade_escolar.models import Aula


class AulaRepository:

    def upsert(self, aula: Aula):
        with Session(engine) as session:
            aula_db = session.query(Aula).filter(
                Aula.id_grade == aula.id_grade, Aula.aula == aula.aula, Aula.dia == aula.dia
            ).first()
            if aula_db == None:
                session.add(aula)
            else:
                aula_db.id_disciplina = aula.id_disciplina

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
