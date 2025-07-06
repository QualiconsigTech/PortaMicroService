from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import disparar_integracao, listar_logs
from .serializers import LogIntegracaoSerializer

class DispararIntegracaoView(APIView):
    def post(self, request):
        log = disparar_integracao(request.data)
        return Response(LogIntegracaoSerializer(log).data, status=status.HTTP_201_CREATED)

class ListarLogsView(APIView):
    def get(self, request):
        logs = listar_logs()
        return Response(LogIntegracaoSerializer(logs, many=True).data)
