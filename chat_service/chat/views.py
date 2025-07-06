from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import enviar_mensagem, listar_conversa
from .serializers import MensagemSerializer

class EnviarMensagemView(APIView):
    def post(self, request):
        mensagem = enviar_mensagem(request.data)
        return Response(MensagemSerializer(mensagem).data, status=status.HTTP_201_CREATED)

class ConversaEntreUsuariosView(APIView):
    def get(self, request):
        origem = request.query_params.get('usuario1')
        destino = request.query_params.get('usuario2')
        if not origem or not destino:
            return Response({"erro": "Parametros usuario1 e usuario2 obrigatorios."}, status=400)
        mensagens = listar_conversa(origem, destino)
        return Response(MensagemSerializer(mensagens, many=True).data)

