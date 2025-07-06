from rest_framework import serializers
from .models import Solicitacao, ComentarioSolicitacao

class SolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitacao
        fields = '__all__'

class ComentarioSolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentarioSolicitacao
        fields = '__all__'
