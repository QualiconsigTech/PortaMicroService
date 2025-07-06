from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import requests



class UsuarioPorIdProxyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            token = request.headers.get("Authorization")
            response = requests.get(
                f'http://localhost:8001/api/usuarios/{id}/',
                headers={'Authorization': token}
            )
            return Response(response.json(), status=response.status_code)
        except Exception as e:
            return Response({'erro': str(e)}, status=500)


class LoginProxyView(APIView):
    def post(self, request):
        try:
            response = requests.post(
                'http://localhost:8001/api/usuarios/login/',
                json=request.data
            )
            return Response(response.json(), status=response.status_code)
        except Exception as e:
            return Response({'erro': str(e)}, status=500)


class CriarChamadoProxyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = request.headers.get("Authorization")
            response = requests.post(
                'http://localhost:8002/api/chamados/criar/',
                json=request.data,
                headers={'Authorization': token}
            )
            return Response(response.json(), status=response.status_code)
        except Exception as e:
            return Response({'erro': str(e)}, status=500)