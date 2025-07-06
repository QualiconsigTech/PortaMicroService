from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .services import *
from .models import Solicitacao
from rest_framework.permissions import IsAuthenticated

class CriarSolicitacaoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        solicitacao = criar_solicitacao(request.data, request.user)
        return Response(SolicitacaoSerializer(solicitacao).data, status=status.HTTP_201_CREATED)


class ComentarioSolicitacaoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        comentario = comentar_solicitacao(request.data, request.user)
        return Response(ComentarioSolicitacaoSerializer(comentario).data, status=status.HTTP_201_CREATED)


class AprovarSolicitacaoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, solicitacao_id):
        solicitacao = Solicitacao.objects.get(id=solicitacao_id)
        aprovacao = aprovar_solicitacao(solicitacao)
        return Response(SolicitacaoSerializer(aprovacao).data)


class EncerrarSolicitacaoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, solicitacao_id):
        solicitacao = Solicitacao.objects.get(id=solicitacao_id)
        encerrada = encerrar_solicitacao(solicitacao)
        return Response(SolicitacaoSerializer(encerrada).data)

