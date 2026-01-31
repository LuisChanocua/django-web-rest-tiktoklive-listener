from rest_framework import serializers
from ..models import TikTokStreamer, TikTokListenerConfig

class ActiveStreamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TikTokStreamer
        fields = ["username"]  # lo que necesita el listener