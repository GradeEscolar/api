from sqlalchemy import create_engine, text
from configparser import ConfigParser
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String
    
config = ConfigParser()
config.read('config.ini')

mysql_env = config['mysql']['env']
mysql_config = config[mysql_env]

user = mysql_config['user']
password = mysql_config['password']
host = mysql_config['host']
database = mysql_config['database']
conn_str = f'mysql://{user}:{password}@{host}/{database}'

mysql_config = {
  'user': user,
  'password': password,
  'host': host,
  'database': database,
  'raise_on_warnings': True
}

engine = create_engine(conn_str, echo=True)

class BaseModel(DeclarativeBase):
  pass

class Usuario(BaseModel):
    __tablename__ = 'usuarios'
    id = Column(Integer,  primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    senha = Column(String(10), nullable=False)
    
    def __repr__(self):
        return f'Usuario(id={self.id}, nome={self.nome}, email={self.email}, senha=***)'
      
BaseModel.metadata.create_all(engine)