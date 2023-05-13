from ..data_context import Usuario

def usuario_to_dict(usuario: Usuario):
    return {
        'id': usuario.id,
        'nome': usuario.nome,
        'email': usuario.email,
        'senha': usuario.senha,
        'data_cadastro': usuario.data_cadastro
    }
    
def dict_to_class (obj, dict):
    for key in dict:
        if(hasattr(obj, key)):
            setattr(obj, key, dict[key])
            
    return obj
    