from rest_framework import viewsets, permissions, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from .models import Usuario
from .serializers import (UsuarioSerializer, UsuarioLogadoSerializer, UsuarioBasicoSerializer, CustomTokenObtainPairSerializer)
from .services import *
from .permissions import IsAdmin, IsSelfOrAdmin
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from core_service.core.permissions import AllowOnlyGateway



class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter(deletado=False)
    serializer_class = UsuarioSerializer
    permission_classes = []

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome', 'email']
    filterset_fields = ['tipo', 'setor_id', 'cargo_id']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deletado = True
        instance.save()
        return Response({"mensagem": "Usuário deletado com sucesso."}, status=status.HTTP_200_OK)
    
    def get_permissions(self):
        if self.action in ['list', 'destroy']:
            return [IsAuthenticated(), IsAdmin()]
        elif self.action in ['update', 'partial_update']:
            return [IsAuthenticated(), IsSelfOrAdmin()]
        return [IsAuthenticated()]


class LoginView(APIView):
    def post(self, request):
        try:
            resultado = autenticar_usuario(
                request.data.get('email'),
                request.data.get('password')
            )
            return Response(resultado, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        

class UsuarioLogadoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        usuario = obter_usuario_logado(request.user)
        serializer = UsuarioLogadoSerializer(usuario)
        return Response(serializer.data)


class AtualizarSenhaView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        nova_senha = request.data.get("senha")
        try:
            resultado = alterar_senha(request.user, nova_senha)
            return Response(resultado)
        except ValidationError as e:
            return Response({"erro": str(e)}, status=400)
        

class UsuarioDadosBasicosView(APIView):
    def get(self, request, id):
        try:
            usuario = Usuario.objects.get(id=id, deletado=False)
            serializer = UsuarioBasicoSerializer(usuario)
            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response({"erro": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)


class UsuarioDadosCompletosView(APIView):
    def get(self, request, id):
        try:
            usuario = Usuario.objects.get(id=id, deletado=False)
            setor = buscar_setor_por_id(usuario.setor_id)
            cargo = buscar_cargo_por_id(usuario.cargo_id)
            grupos = buscar_grupos_por_ids(usuario.grupo_ids)

            return Response({
                "id": usuario.id,
                "nome": usuario.nome,
                "email": usuario.email,
                "setor": setor.get("nome"),
                "cargo": cargo.get("nome"),
                "grupos": [g["nome"] for g in grupos if isinstance(g, dict) and "nome" in g]
            })
        except Usuario.DoesNotExist:
            return Response({"erro": "Usuário não encontrado"}, status=404)
        
class UsuarioDadosBasicosView(APIView):
    def get(self, request, id):
        try:
            usuario = Usuario.objects.get(id=id, deletado=False)
            serializer = UsuarioBasicoSerializer(usuario)
            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response({'erro': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

# usuarios/views.py
class BuscarUsuarioPorIdView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        usuario = get_object_or_404(Usuario, id=id, deletado=False)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

class CustomTokenView(TokenObtainPairView):
    permission_classes = [AllowOnlyGateway]
