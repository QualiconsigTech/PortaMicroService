from rest_framework import serializers

class UsuarioLogadoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField()
    email = serializers.EmailField()
    tipo = serializers.CharField(required=False)
    is_admin = serializers.BooleanField()
