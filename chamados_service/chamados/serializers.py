from rest_framework import serializers
from chamados.models import Chamado

class ChamadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamado
        fields = '__all__'
