from ..data_context import Usuario

def usuario_to_dict(usuario: Usuario):
    return {
        'id': usuario.id,
        'nome': usuario.nome,
        'email': usuario.email,
        'senha': usuario.senha
    }