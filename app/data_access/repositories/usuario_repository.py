import json
from app.data_access.models.usuario import Usuario
from app.data_access import session_maker, mysql_config
import mysql.connector

class UsuarioRepository:
        
    def listar_sqlalchemy(self):
        session = session_maker()
        usuarios_db =  session.query(Usuario).all() #[{'a': 1}]
        session.close()
        usuarios = [usuario_db.as_dict for usuario_db in usuarios_db]    
        print(usuarios)
        return usuarios
    
    def listar_mysql_connector(self):
        with mysql.connector.connect(**mysql_config) as conn:
            with conn.cursor(dictionary=True) as cr:
                query = 'select * from usuarios'
                cr.execute(query)
                usuarios = [row for row in cr]    
                cr.close()
            conn.close()
        return usuarios