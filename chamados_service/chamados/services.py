from chamados.models import Chamado
from chamados.serializers import ChamadoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
import requests

def listar_chamados_do_usuario(usuario_id):
    return Chamado.objects.filter(usuario_id=usuario_id).order_by('-criado_em')

def criar_chamado(data, usuario):
    data = data.copy()
    data['usuario_id'] = usuario.id
    serializer = ChamadoSerializer(data=data)
    
    if serializer.is_valid():
        chamado = serializer.save()
        return chamado, None
    else:
        return None, serializer.errors

class ChamadoViewSet(viewsets.ModelViewSet):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer
    permission_classes = [IsAuthenticated]


def buscar_dados_usuario(user_id):
    try:
        response = requests.get(f'http://localhost:8001/api/usuarios/{user_id}/')
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException:
        return None
