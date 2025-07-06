from rest_framework import serializers
from .models import LogIntegracao

class LogIntegracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogIntegracao
        fields = '__all__'
