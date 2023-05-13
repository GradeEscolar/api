from datetime import datetime, timedelta, timezone
from sqlalchemy import CheckConstraint, create_engine, func, text
from configparser import ConfigParser
from sqlalchemy.orm import Session, DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime
from typing import TypeVar, Any
    
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

T = TypeVar("T")

def to_dict(obj:T) -> dict[str, Any]:
  dic = dict[str, Any]()
  for key in vars(obj).items():
    if key[0] != '_sa_instance_state':
      dic[key[0]] = key[1]
  return dic  
        
def from_dict(obj:T, dic:dict[str, Any]) -> None:
    for key in dic:
        if(hasattr(obj, key)):
            setattr(obj, key, dic[key])
            
def get_keys(obj:T):
  return [k for k in obj.__dict__ if not(k[0].startswith('_'))]

engine = create_engine(conn_str, echo=True)
  
class BaseModel(DeclarativeBase):
  pass

class Usuario(BaseModel):
  __tablename__ = 'usuarios'
  
  id = Column(Integer,  primary_key=True, autoincrement=True)
  nome = Column(String(30), nullable=False)
  email = Column(String(50), unique=True, nullable=False)
  senha = Column(String(10), nullable=False)
  data_cadastro = Column(DateTime(True), nullable=False)
      
  def __repr__(self):
    return f'Usuario(id={self.id}, nome={self.nome}, email={self.email}, senha=***)'
    
  to_dict = lambda self: to_dict(self)
  from_dict = lambda self, dict: from_dict(self, dict)
  
  def set_data_cadastro(self):
    dt = datetime.utcnow() - timedelta(hours=3)
    self.data_cadastro = dt
    
  
BaseModel.metadata.drop_all(engine)
BaseModel.metadata.create_all(engine)

