from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        usuario = request.user
        return Response({
            "id": usuario.id,
            "nome": usuario.get_full_name() or usuario.username,
            "email": usuario.email,
            "is_admin": usuario.is_staff,
        })

