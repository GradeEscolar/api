from sqlalchemy import Column, Integer, String, inspect
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Usuario(base):
    __tablename__ = 'usuarios'
    id = Column(Integer,  primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    senha = Column(String(10), nullable=False)
    
    def __repr__(self):
        return f'Usuario(id={self.id}, nome={self.nome}, email={self.email}, senha=***)'
    
    def to_dic(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha
        }
        
    @property
    def as_dict(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}