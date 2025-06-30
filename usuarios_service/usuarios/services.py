from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from .models import Usuario
import requests

def criar_usuario(data):
    senha = data.pop('senha', None)
    grupos = data.pop('grupo_ids', [])
    usuario = Usuario(**data)
   
    if senha:
        usuario.set_password(senha)
    usuario.save()

    if grupos:
        usuario.grupo_ids = grupos
        usuario.save()

    return usuario


def atualizar_usuario(usuario, data):
    senha = data.pop('senha', None)
    for attr, value in data.items():
        setattr(usuario, attr, value)
    if senha:
        usuario.set_password(senha)
    usuario.save()
    return usuario


def autenticar_usuario(email, password):
    usuario = authenticate(email=email, password=password)
    if not usuario:
        raise AuthenticationFailed("Credenciais inválidas.")

    refresh = RefreshToken.for_user(usuario)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def obter_usuario_logado(usuario):
    return usuario 

def alterar_senha(usuario, nova_senha):
    if not nova_senha or len(nova_senha) < 6:
        raise ValidationError("A nova senha deve ter pelo menos 6 caracteres.")
    
    usuario.set_password(nova_senha)
    usuario.save()
    return {"mensagem": "Senha atualizada com sucesso."}


CORE_BASE_URL = "http://localhost:8001/api"

def buscar_setor_por_id(setor_id):
    try:
        url = f"{CORE_BASE_URL}/setores/{setor_id}/"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.json()
        return {"erro": "Setor não encontrado"}
    except requests.RequestException:
        return {"erro": "Erro de comunicação com core_service"}
    
def buscar_cargo_por_id(cargo_id):
    try:
        url = f"{CORE_BASE_URL}/cargos/{cargo_id}/"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.json()
        return {"erro": "Cargo não encontrado"}
    except requests.RequestException:
        return {"erro": "Erro de comunicação com core_service"}

def buscar_grupos_por_ids(grupo_ids):
    try:
        ids_str = ",".join(str(i) for i in grupo_ids)
        url = f"{CORE_BASE_URL}/grupos/?ids={ids_str}"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.json() 
        return {"erro": "Grupos não encontrados"}
    except requests.RequestException:
        return {"erro": "Erro de comunicação com core_service"}