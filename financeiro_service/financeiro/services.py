from .models import Repassse
from .serializers import RepassseSerializer
from rest_framework.exceptions import ValidationError

def criar_repasse(data):
    serializer = RepassseSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()

def listar_repasses(usuario_id=None):
    queryset = Repassse.objects.all().order_by('-criado_em')
    if usuario_id:
        queryset = queryset.filter(usuario_id=usuario_id)
    return queryset
