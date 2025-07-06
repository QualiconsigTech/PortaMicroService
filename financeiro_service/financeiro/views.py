from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import criar_repasse, listar_repasses
from .serializers import RepassseSerializer

class CriarRepasseView(APIView):
    def post(self, request):
        repasse = criar_repasse(request.data)
        return Response(RepassseSerializer(repasse).data, status=status.HTTP_201_CREATED)


class ListarRepassesView(APIView):
    def get(self, request):
        usuario_id = request.query_params.get('usuario_id')
        repasses = listar_repasses(usuario_id)
        return Response(RepassseSerializer(repasses, many=True).data)

