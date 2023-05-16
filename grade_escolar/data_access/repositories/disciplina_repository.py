import datetime
from sqlalchemy.orm import Session
from sqlalchemy import Exists, select
from mysql import connector
from grade_escolar.data_access import engine, mysql_config
from grade_escolar.data_access.models import Disciplina

class DisciplinaRepository:
    
    def create(self, disciplina: Disciplina):    
        with Session(engine) as session:
            query = session.query(Disciplina).filter(Disciplina.id_usuario == disciplina.id_usuario and Disciplina.disciplina == disciplina.disciplina)
            exists = session.query(query.exists()).scalar()
            if(not(exists)):
                session.add(disciplina)
                session.commit()
                return True
            else:
                return False
            
    def read(self, id_usuario: int):
        with Session(engine) as session:
            return session.query(Disciplina).filter(Disciplina.id_usuario == id_usuario).all()