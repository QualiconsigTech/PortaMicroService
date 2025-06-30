from django.contrib.auth.models import AbstractBaseUser
from typing import Union

def get_usuario_logado(usuario: Union[AbstractBaseUser, any]) -> dict:
    return {
        "id": usuario.id,
        "nome": getattr(usuario, 'nome', usuario.get_full_name() or usuario.username),
        "email": getattr(usuario, 'email', ''),
        "tipo": getattr(usuario, 'tipo', None),
        "is_admin": getattr(usuario, 'is_staff', False),
    }
