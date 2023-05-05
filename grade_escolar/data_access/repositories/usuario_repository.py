import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select
from mysql import connector
from grade_escolar.data_access import engine, mysql_config
from grade_escolar.data_access.models import Usuario, usuario_to_dict

class UsuarioRepository:
    
    def create(self, usuario: Usuario):
        with Session(engine) as session:
            session.add(usuario)
            session.commit()
            
    def listar(self):
        with Session(engine) as session:
            usuarios = session.query(Usuario).all()
            usuarios_dict = [usuario_to_dict(usuario) for usuario in usuarios]
            return usuarios_dict
        
    
    def listar_mysql_connector(self):
        with connector.connect(**mysql_config) as conn:
            with conn.cursor(dictionary=True) as cr:
                query = 'select * from usuarios'
                cr.execute(query)
                usuarios = [row for row in cr]    
                cr.close()
            conn.close()
        return usuarios