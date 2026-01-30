# app_tiktok/serializers.py
from rest_framework import serializers
from ..models import TikTokComment, TikTokStreamer

class TikTokCommentInSerializer(serializers.Serializer):
    streamer_username = serializers.CharField(max_length=64)

    tiktok_user_id = serializers.CharField(max_length=128)
    tiktok_nickname = serializers.CharField(max_length=128, allow_blank=True)
    tiktok_profile_picture = serializers.URLField(required=False, allow_blank=True)

    text = serializers.CharField()
    tiktok_comment_id = serializers.CharField(max_length=128, required=False, allow_blank=True)
    tiktok_timestamp = serializers.DateTimeField(required=False)

    raw_payload = serializers.JSONField(required=False)

    def create(self, validated_data):
        streamer_username = validated_data.pop("streamer_username")

        streamer, _ = TikTokStreamer.objects.get_or_create(
            username=streamer_username
        )

        comment = TikTokComment.objects.create(
            streamer=streamer,
            **validated_data
        )
        return comment
