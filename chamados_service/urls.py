from django.urls import path, include

urlpatterns = [
    path('api/chamados/', include('chamados.urls')),
]
