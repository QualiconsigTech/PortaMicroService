from rest_framework import viewsets, status
from chamados.models import Chamado
from chamados.serializers import ChamadoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from chamados.services import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from core_service.core.permissions import AllowOnlyGateway


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
        # Extrai user_id do token JWT sem depender de request.user
        jwt_authenticator = JWTAuthentication()
        try:
            validated_token = jwt_authenticator.get_validated_token(request.auth)
            user_id = validated_token.get('user_id')
        except Exception:
            return Response({'erro': 'Token inválido'}, status=401)

        # Toda a lógica continua no services.py
        chamado, errors = criar_chamado(request.data, user_id)

        if errors:
            return Response({'errors': errors}, status=400)
        return Response({'mensagem': 'Chamado criado com sucesso'}, status=201)

class CustomTokenView(TokenObtainPairView):
    permission_classes = [AllowOnlyGateway]
