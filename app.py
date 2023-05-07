from grade_escolar import app_server as application

if __name__ == '__main__':
    application.run(host="0.0.0.0", debug=False)

#from datetime import datetime, timedelta, timezone
#import inspect
#import json
#
##tz = timezone('America/Sao_Paulo')
#
##dt = datetime.utcnow()
##dt = dt - timedelta(hours=3)
##print(dt)
##print(dt.tzinfo)
##

#from typing import Any, TypeVar
#
#T = TypeVar("T")
#
#def to_dict(obj:T) -> dict[str, Any]:
#    d = dict()
#    for k in obj.__annotations__:
#        d[k] = getattr(obj, k, None)
#    return d
#        
#def from_dict(obj:T, dict:dict[str, Any]) -> None:
#    for key in obj.__annotations__:
#        if dict.__contains__(key):
#            setattr(obj, key, dict[key])
#    
#class Pessoa:
#    nome: str
#    idade: int
#    
#    to_dict = lambda self: to_dict(self)
#    from_dict = lambda self, dict: from_dict(self, dict)
#    
#pessoa = Pessoa()
#
#n = dict()
#n["nome"] = "b"
#n["idade"] = 1
#n["peso"] = 1
#
#pessoa.from_dict(n)
#
#print(pessoa.nome)
#print(pessoa.idade)
#
#d = pessoa.to_dict()
#print(d)
#
