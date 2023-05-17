from sqlalchemy.orm import Session
from grade_escolar.data_access import engine
from grade_escolar.models import Disciplina

class DisciplinaRepository:

    def create(self, disciplina: Disciplina):
        with Session(engine) as session:
            query = session.query(Disciplina).filter(
                Disciplina.id_usuario == disciplina.id_usuario, Disciplina.disciplina == disciplina.disciplina)
            exists = session.query(query.exists()).scalar()
            if (not (exists)):
                session.add(disciplina)
                session.commit()
                return True
            else:
                return False

    def read(self, id_usuario: int):
        with Session(engine) as session:
            return session.query(Disciplina).filter(Disciplina.id_usuario == id_usuario).all()

    def exists_id(self, id_usuario: int, id: int):
        with Session(engine) as session:
            query = session.query(Disciplina).filter(Disciplina.id_usuario == id_usuario, Disciplina.id == id)
            return session.query(query.exists()).scalar()

    def exists_disciplina(self, id_usuario: int, disciplina: str):
        with Session(engine) as session:
            query = session.query(Disciplina).filter(Disciplina.id_usuario == id_usuario, Disciplina.disciplina == disciplina)
            return session.query(query.exists()).scalar()
    
    def update(self, id: int, disciplina: str):
        with Session(engine) as session:        
            d = session.get(Disciplina, id)
            d.disciplina = disciplina
            session.commit()
            
    def delete(self, id: int):
        with Session(engine) as session:
            disciplina = session.get(Disciplina, id)
            session.delete(disciplina)
            session.commit()