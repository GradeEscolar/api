from configparser import ConfigParser
from datetime import datetime
from sqlalchemy import Index, Integer, String, DateTime, Text, create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from typing import List, TypeVar, Any
    
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
  
  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  nome: Mapped[str] = mapped_column(String(30), nullable=False)
  email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
  senha: Mapped[str] = mapped_column(String(60), nullable=False)
  data_cadastro: Mapped[datetime] = mapped_column(DateTime(True), nullable=False)
  
  _grade: Mapped['Grade'] = relationship("Grade", back_populates='_usuario', uselist=False, lazy='select', cascade='all, delete-orphan')
  _disciplinas: Mapped[List['Disciplina']] = relationship("Disciplina", back_populates='_usuario', uselist=True, lazy='select', cascade='all, delete-orphan')
  
  to_dict = lambda self: to_dict(self)
  from_dict = lambda self, dict: from_dict(self, dict)
  to_str = lambda self: to_str(self)
  def __repr__(self) -> str:
    return self.to_str()
    
class Grade(BaseModel):
  __tablename__ = 'grade'
  
  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  id_usuario: Mapped[int] = mapped_column(Integer, ForeignKey(Usuario.id, ondelete='CASCADE'), nullable=False)
  aulas: Mapped[int] = mapped_column(Integer, nullable=False)
  dias: Mapped[str] = mapped_column(String(14), nullable=False)
  
  _usuario: Mapped[Usuario] = relationship('Usuario', back_populates='_grade', lazy='select')
  _aulas: Mapped[List['Aula']] = relationship("Aula", back_populates='_grade', uselist=True, lazy='select')
  
  to_dict = lambda self: to_dict(self)
  from_dict = lambda self, dict: from_dict(self, dict)
  to_str = lambda self: to_str(self)
  def __repr__(self) -> str:
    return self.to_str()
  
class Disciplina(BaseModel):
  __tablename__ = 'disciplinas'
  
  id: Mapped[int] = mapped_column(Integer,  primary_key=True, autoincrement=True)
  id_usuario: Mapped[int] = mapped_column(Integer, ForeignKey(Usuario.id, ondelete='CASCADE'), nullable=False)
  disciplina: Mapped[str] = mapped_column(String(50), nullable=False)
  
  _usuario: Mapped[Usuario] = relationship('Usuario', back_populates='_disciplinas', lazy='select')
  _anotacoes: Mapped[List['Anotacao']] = relationship("Anotacao", back_populates='_disciplina', uselist=True, lazy='select', cascade='all, delete-orphan')
  _aulas: Mapped[List['Aula']] = relationship("Aula", back_populates='_disciplina', uselist=True, lazy='select', cascade='all, delete-orphan')
  
  to_dict = lambda self: to_dict(self)
  from_dict = lambda self, dict: from_dict(self, dict)
  to_str = lambda self: to_str(self)
  def __repr__(self) -> str:
    return self.to_str()
  
class Anotacao(BaseModel):
  __tablename__ = 'anotacoes'
  
  id: Mapped[int] = mapped_column(Integer,  primary_key=True, autoincrement=True)
  id_disciplina: Mapped[int] = mapped_column(Integer, ForeignKey(Disciplina.id, ondelete='CASCADE'), nullable=False)
  aula: Mapped[int] = mapped_column(Integer, nullable=False)
  data: Mapped[datetime] = mapped_column(DateTime(True), nullable=False)
  anotacao: Mapped[str] = mapped_column(Text, nullable=True)
  
  _disciplina: Mapped[Disciplina] = relationship('Disciplina', back_populates='_anotacoes', lazy='select')
      
  to_dict = lambda self: to_dict(self)
  from_dict = lambda self, dict: from_dict(self, dict)
  to_str = lambda self: to_str(self)
  def __repr__(self) -> str:
    return self.to_str()

class Aula(BaseModel):
  __tablename__ = 'aulas'
  
  id: Mapped[int] = mapped_column(Integer,  primary_key=True, autoincrement=True)
  id_grade: Mapped[int] = mapped_column(Integer, ForeignKey(Grade.id, ondelete='CASCADE'), nullable=False)
  id_disciplina: Mapped[int] = mapped_column(Integer, ForeignKey(Disciplina.id, ondelete='CASCADE'), nullable=False)
  aula: Mapped[int] = mapped_column(Integer, nullable=False)
  dia: Mapped[int] = mapped_column(Integer, nullable=False)

  _grade: Mapped[List['Grade']] = relationship("Grade", back_populates='_aulas', uselist=True, lazy='select')
  _disciplina: Mapped[List['Disciplina']] = relationship("Disciplina", back_populates='_aulas', uselist=True, lazy='select')

  to_dict = lambda self: to_dict(self)
  from_dict = lambda self, dict: from_dict(self, dict)
  to_str = lambda self: to_str(self)
  def __repr__(self) -> str:
    return self.to_str()

disciplinas_uidx_usuario_disciplina = Index('disciplinas_uidx_usuario_disciplina', Disciplina.id_usuario, Disciplina.disciplina, unique=True)
anotacao_uidx_disciplina_aula_data = Index('anotacao_uidx_disciplina_aula_data', Anotacao.id_disciplina, Anotacao.aula, Anotacao.data, unique=True)
aulas_uidx_grade_aula_dia = Index('aulas_uidx_grade_aula_dia', Aula.id_grade, Aula.aula, Aula.dia, unique=True)
aulas_idx_grade_dia = Index('aulas_idx_grade_dia', Aula.id_grade, Aula.dia, unique=False)

if mysql_reset == 's':
  BaseModel.metadata.drop_all(engine)

BaseModel.metadata.create_all(engine)
