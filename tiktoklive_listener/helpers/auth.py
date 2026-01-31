# app_tiktok/auth.py
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

def validate_internal_token(request):
    token = request.headers.get("X-Internal-Token")
    if not token or token != getattr(settings, "INTERNAL_LISTENER_TOKEN", None):
        return Response({"detail": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
    return None
