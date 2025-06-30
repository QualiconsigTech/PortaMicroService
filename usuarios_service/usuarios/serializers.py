from rest_framework import serializers
from .models import Usuario
from .services import criar_usuario, atualizar_usuario

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
