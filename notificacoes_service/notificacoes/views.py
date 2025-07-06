from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import criar_notificacao, listar_notificacoes
from .serializers import NotificacaoSerializer

class CriarNotificacaoView(APIView):
    def post(self, request):
        notificacao = criar_notificacao(request.data)
        return Response(NotificacaoSerializer(notificacao).data, status=status.HTTP_201_CREATED)


class MinhasNotificacoesView(APIView):
    def get(self, request):
        usuario_id = request.query_params.get("usuario_id")
        if not usuario_id:
            return Response({"erro": "Parametro usuario_id obrigatorio."}, status=400)
        notificacoes = listar_notificacoes(usuario_id)
        return Response(NotificacaoSerializer(notificacoes, many=True).data)
