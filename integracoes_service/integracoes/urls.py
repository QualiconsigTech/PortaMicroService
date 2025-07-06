from django.urls import path
from .views import DispararIntegracaoView, ListarLogsView

urlpatterns = [
    path('disparar/', DispararIntegracaoView.as_view()),
    path('logs/', ListarLogsView.as_view()),
]