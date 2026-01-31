from rest_framework import serializers

class ListenerToggleSerializer(serializers.Serializer):
    enabled = serializers.BooleanField()