from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GrupoViewSet, SetorViewSet, CargoViewSet

router = DefaultRouter()
router.register(r'grupos', GrupoViewSet)
router.register(r'setores', SetorViewSet)
router.register(r'cargos', CargoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]