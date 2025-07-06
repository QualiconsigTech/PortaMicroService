from django.shortcuts import render
from rest_framework import viewsets
from .models import Grupo, Setor, Cargo
from .serializers import *
from .permissions import AllowOnlyGateway
from rest_framework_simplejwt.views import TokenObtainPairView

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer


class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.select_related('grupo').all()
    serializer_class = SetorSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class CustomTokenView(TokenObtainPairView):
    permission_classes = [AllowOnlyGateway]
