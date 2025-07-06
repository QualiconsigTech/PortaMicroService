from rest_framework import serializers
from .models import Repassse

class RepassseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repassse
        fields = '__all__'