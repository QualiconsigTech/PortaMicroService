from django.urls import path
from .views import CriarRepasseView, ListarRepassesView

urlpatterns = [
    path('criar/', CriarRepasseView.as_view()),
    path('listar/', ListarRepassesView.as_view()),
]
