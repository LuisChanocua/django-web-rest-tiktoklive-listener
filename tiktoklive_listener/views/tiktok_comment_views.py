# app_tiktok/views/tiktok_comment_views.py
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import TikTokCommentInSerializer

class TikTokCommentInView(APIView):
    authentication_classes = []  # usamos token interno, no auth de usuarios
    permission_classes = []

    def post(self, request, *args, **kwargs):
        # 1) Validar token interno
        internal_token = request.headers.get("X-Internal-Token")
        if internal_token != settings.INTERNAL_LISTENER_TOKEN:
            return Response({"detail": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        # 2) Validar payload
        serializer = TikTokCommentInSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # 3) Crear comentario
        comment = serializer.save()

        return Response(
            {"id": comment.id},
            status=status.HTTP_201_CREATED
        )
