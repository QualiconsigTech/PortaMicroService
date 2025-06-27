from rest_framework import serializers
from .models import Grupo, Setor, Cargo


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = ['id', 'nome']


class SetorSerializer(serializers.ModelSerializer):
    grupo = GrupoSerializer(read_only=True)
    grupo_id = serializers.PrimaryKeyRelatedField(
        queryset=Grupo.objects.all(), source='grupo', write_only=True
    )

    class Meta:
        model = Setor
        fields = ['id', 'nome', 'grupo', 'grupo_id']


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['id', 'nome']
