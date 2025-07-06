from .models import Solicitacao, ComentarioSolicitacao
from .serializers import SolicitacaoSerializer, ComentarioSolicitacaoSerializer
from rest_framework.exceptions import ValidationError
from django.utils import timezone

def criar_solicitacao(data, usuario):
    data = data.copy()
    data["usuario_id"] = usuario.id
    serializer = SolicitacaoSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()

def comentar_solicitacao(data, usuario):
    data = data.copy()
    data["usuario_id"] = usuario.id
    serializer = ComentarioSolicitacaoSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()


def aprovar_solicitacao(solicitacao):
    solicitacao.aprovado = True
    solicitacao.save()
    return solicitacao


def encerrar_solicitacao(solicitacao):
    if solicitacao.encerrado_em:
        raise ValidationError("Solicitação já encerrada.")
    solicitacao.encerrado_em = timezone.now()
    solicitacao.save()
    return solicitacao