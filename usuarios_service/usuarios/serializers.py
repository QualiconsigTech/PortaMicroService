from rest_framework import serializers
from .services import criar_usuario, atualizar_usuario
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Usuario
        fields = [
            'id', 'nome', 'email', 'senha', 'tipo',
            'setor_id', 'cargo_id', 'grupo_ids',
            'is_admin', 'is_staff', 'is_active',
            'ultimo_acesso', 'deletado'
        ]
        read_only_fields = ['id', 'is_staff', 'is_active', 'deletado', 'ultimo_acesso']



    def create(self, validated_data):
        return criar_usuario(validated_data)

    def update(self, instance, validated_data):
        return atualizar_usuario(instance, validated_data)

class UsuarioLogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'tipo', 'setor_id', 'cargo_id', 'grupo_ids', 'is_admin', 'deletado']

class UsuarioBasicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'tipo', 'setor_id']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        print("DEBUG login:")
        print("email:", email)
        print("password:", password)

        user = authenticate(username=email, password=password)
        if user is None:
            raise AuthenticationFailed("Email ou senha inválidos.")

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'usuario_id': user.id,
            'nome': user.nome,
            'email': user.email,
        }

    @classmethod
    def get_token(cls, user):
        return super().get_token(user)