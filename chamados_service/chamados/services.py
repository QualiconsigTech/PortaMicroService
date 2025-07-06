from chamados.models import Chamado
from chamados.serializers import ChamadoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
import requests

def listar_chamados_do_usuario(usuario_id):
    return Chamado.objects.filter(usuario_id=usuario_id).order_by('-criado_em')

def buscar_dados_usuario(user_id):
    try:
        response = requests.get(f'http://localhost:8001/api/usuarios/{user_id}/')
        if response.status_code == 200:
            return response.json()
    except Exception:
        return None
    return None

def criar_chamado(data, user_id):
    dados_usuario = buscar_dados_usuario(user_id)
    if not dados_usuario:
        return None, {'usuario': 'Usuário não encontrado.'}

    data = data.copy()
    data['usuario_id'] = user_id

    serializer = ChamadoSerializer(data=data)
    if serializer.is_valid():
        chamado = serializer.save()
        return chamado, None
    return None, serializer.errors

