# app_tiktok/views.py
import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import TikTokStreamer, TikTokListenerConfig
from ..serializers import ActiveStreamerSerializer, ListenerToggleSerializer
from ..helpers.auth import validate_internal_token


class ActiveListenerStreamersView(APIView):
    """
    Devuelve los streamers que el listener debe escuchar.
    El listener la consulta periódicamente.
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        # Token interno
        auth_error = validate_internal_token(request)
        if auth_error:
            return auth_error

        qs = TikTokStreamer.objects.filter(
            is_active=True,
            should_listen=True,
        ).order_by("username")

        serializer = ActiveStreamerSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListenerToggleView(APIView):
    """
    GET: devuelve el estado actual del listener global (enabled).
    POST: actualiza el estado (enabled true/false).
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        auth_error = validate_internal_token(request)
        if auth_error:
            return auth_error

        config = TikTokListenerConfig.get_solo()
        return Response({"enabled": config.enabled}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        auth_error = validate_internal_token(request)
        if auth_error:
            return auth_error

        serializer = ListenerToggleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        config = TikTokListenerConfig.get_solo()
        config.enabled = serializer.validated_data["enabled"]
        config.save()

        return Response({"enabled": config.enabled}, status=status.HTTP_200_OK)
