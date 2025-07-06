from .models import Notificacao
from .serializers import NotificacaoSerializer
from rest_framework.exceptions import ValidationError

def criar_notificacao(data):
    serializer = NotificacaoSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()


def listar_notificacoes(usuario_id):
    return Notificacao.objects.filter(usuario_destino_id=usuario_id).order_by('-criado_em')
