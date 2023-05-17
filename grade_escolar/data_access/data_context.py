from configparser import ConfigParser
from sqlalchemy import Column, Integer, String, DateTime, Text, UniqueConstraint, create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from typing import TypeVar, Any
    
config = ConfigParser()
config.read('config.ini')

mysql_env = config['mysql']['env']
mysql_reset = config['mysql']['reset']
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
    if not key[0].startswith("_"):
      dic[key[0]] = key[1]
  return dic  
        
def from_dict(obj:T, dic:dict[str, Any]) -> None:
    for key in dic:
        if(hasattr(obj, key) and not key.startswith("_")):
            setattr(obj, key, dic[key])
            
def get_keys(obj:T):
  return [k for k in obj.__dict__ if not(k[0].startswith("_"))]

def to_str(obj:T):
  values = []
  dic = to_dict(obj)
  for key in dic:
    values.append(f'{key}={dic[key]}')
    
  str_values = ', '.join(values)
  return f'{obj.__class__}({str_values})'
    
engine = create_engine(conn_str, echo=True)
  
class BaseModel(DeclarativeBase):
  pass

class Usuario(BaseModel):
  __tablename__ = 'usuarios'
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  nome = Column(String(30), nullable=False)
  email = Column(String(50), unique=True, nullable=False)
  senha = Column(String(60), nullable=False)
  data_cadastro = Column(DateTime(True), nullable=False)
  
  _grade = relationship("Grade", back_populates='_usuario', uselist=False, lazy='select')
  _disciplinas = relationship("Disciplina", back_populates='_usuario', uselist=True, lazy='select')
  
  to_dict = lambda self: to_dict(self)
  from_dict = lambda self, dict: from_dict(self, dict)
  to_str = lambda self: to_str(self)
  def __repr__(self) -> str:
    return self.to_str()
    
class Grade(BaseModel):
  __tablename__ = 'grade'
  
  id = Column(Integer,  primary_key=True, autoincrement=True)
  id_usuario = Column(Integer, ForeignKey(Usuario.id))
  aulas = Column(Integer, nullable=False)
  dias = Column(String(14), nullable=False)
  
  _usuario = relationship('Usuario', back_populates='_grade', lazy='select')
  
  to_dict = lambda self: to_dict(self)
  from_dict = lambda self, dict: from_dict(self, dict)
  to_str = lambda self: to_str(self)
  def __repr__(self) -> str:
    return self.to_str()
  
class Disciplina(BaseModel):
  __tablename__ = 'disciplinas'
  __table_args__ = (UniqueConstraint('id_usuario', 'disciplina', name='_disciplina_usuario_uc'),)
  
  id = Column(Integer,  primary_key=True, autoincrement=True)
  id_usuario = Column(Integer, ForeignKey(Usuario.id))
  disciplina = Column(String(50), nullable=False)
  
  _usuario = relationship('Usuario', back_populates='_disciplinas', lazy='select')
  _anotacoes = relationship("Anotacao", back_populates='_disciplina', uselist=True, lazy='select')
  
  to_dict = lambda self: to_dict(self)
  from_dict = lambda self, dict: from_dict(self, dict)
  to_str = lambda self: to_str(self)
  def __repr__(self) -> str:
    return self.to_str()
  
class Anotacao(BaseModel):
  __tablename__ = 'anotacoes'
  
  id = Column(Integer,  primary_key=True, autoincrement=True)
  id_disciplina = Column(Integer, ForeignKey(Disciplina.id))
  aula = Column(Integer, nullable=False)
  data = Column(DateTime(True), nullable=False)
  anotacao = Column(Text)
  
  _disciplina = relationship('Disciplina', back_populates='_anotacoes', lazy='select')
        
  to_dict = lambda self: to_dict(self)
  from_dict = lambda self, dict: from_dict(self, dict)
  to_str = lambda self: to_str(self)
  def __repr__(self) -> str:
    return self.to_str()

if mysql_reset == 's':
  BaseModel.metadata.drop_all(engine)

BaseModel.metadata.create_all(engine)

