# permissions.py
from rest_framework.permissions import BasePermission
from django.conf import settings

class AllowOnlyGateway(BasePermission):
    def has_permission(self, request, view):
        origin = request.META.get('HTTP_ORIGIN', '')
        return origin.startswith(settings.GATEWAY_URL)
