import datetime
from sqlalchemy.orm import Session, subqueryload
from sqlalchemy import Exists, select
from mysql import connector
from grade_escolar.data_access import engine, mysql_config
from grade_escolar.models import Usuario

class UsuarioRepository:
    
    def create(self, usuario: Usuario):
        
        with Session(engine) as session:
            query = session.query(Usuario).filter(Usuario.email == usuario.email)
            exists = session.query(query.exists()).scalar()
            if(not(exists)):
                session.add(usuario)
                session.commit()
                return True
            else:
                return False
            
    def listar(self):
        with Session(engine) as session:
            return session.query(Usuario).all()
        
    def obter_login(self, usuario: Usuario):
        with Session(engine) as session:
            return session.query(Usuario).filter(Usuario.email == usuario.email).first()
            
    def listar_mysql_connector(self):
        with connector.connect(**mysql_config) as conn:
            with conn.cursor(dictionary=True) as cr:
                query = 'select * from usuarios'
                cr.execute(query)
                usuarios = [row for row in cr]    
                cr.close()
            conn.close()
        return usuarios