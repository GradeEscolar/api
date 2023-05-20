from sqlalchemy import extract
from sqlalchemy.orm import Session
from grade_escolar.data_access import engine
from grade_escolar.models import Anotacao


class AnotacaoRepository:

    def upsert(self, anotacao: Anotacao):
        with Session(engine) as session:
            anotacao_db = session.query(Anotacao).filter(
                Anotacao.aula == anotacao.aula, Anotacao.id_disciplina == anotacao.id_disciplina, Anotacao.data == anotacao.data
            ).first()

            if anotacao_db == None:
                session.add(anotacao)
            else:
                anotacao_db.anotacao = anotacao.anotacao

            session.commit()

    def read_grade(self, anotacao: Anotacao):
        with Session(engine) as session:
            return session.query(Anotacao).filter(
                Anotacao.aula == anotacao.aula, Anotacao.id_disciplina == anotacao.id_disciplina, Anotacao.data == anotacao.data
            ).first()

    def read_disciplina(self, anotacao: Anotacao):
        with Session(engine) as session:
            return session.query(Anotacao).filter(
                Anotacao.id_disciplina == anotacao.id_disciplina,
                extract('month', Anotacao.data) == extract('month', anotacao.data),
                extract('year', Anotacao.data) == extract('year', anotacao.data)
            ).all()

    def delete(self, id: int):
        with Session(engine) as session:
            anotacao = session.get(Anotacao, id)
            if anotacao:
                session.delete(anotacao)
                session.commit()
