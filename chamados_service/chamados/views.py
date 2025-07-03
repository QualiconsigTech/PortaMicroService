from rest_framework import viewsets, status
from chamados.models import Chamado
from chamados.serializers import ChamadoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from chamados.services import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed

class ChamadoViewSet(viewsets.ModelViewSet):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer


class MeusChamadosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        chamados = listar_chamados_do_usuario(request.user.id)
        serializer = ChamadoSerializer(chamados, many=True)
        return Response(serializer.data)

from rest_framework.permissions import AllowAny  # só para teste

class CriarChamadoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.user.id  # vem do JWT, não depende de buscar no banco
        data = request.data.copy()
        data['usuario_id'] = user_id

        serializer = ChamadoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensagem': 'Chamado criado com sucesso'}, status=201)
        return Response(serializer.errors, status=400)


class CriarChamadoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.user.id
        dados_usuario = buscar_dados_usuario(user_id)

        if not dados_usuario:
            return Response({'erro': 'Usuário não encontrado.'}, status=401)

        data = request.data.copy()
        data['usuario_id'] = user_id

        serializer = ChamadoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensagem': 'Chamado criado com sucesso'}, status=201)
        return Response(serializer.errors, status=400)
