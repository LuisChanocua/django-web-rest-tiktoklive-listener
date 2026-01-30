# app_tiktok/models.py
from django.db import models
from .TikTokStreamer import TikTokStreamer

class TikTokComment(models.Model):
    streamer = models.ForeignKey(
        TikTokStreamer,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    # Usuario de TikTok que comenta
    tiktok_user_id = models.CharField(max_length=128)       # unique_id o sec_uid
    tiktok_nickname = models.CharField(max_length=128)
    tiktok_profile_picture = models.URLField(blank=True)

    # Contenido del comentario
    text = models.TextField()
    raw_payload = models.JSONField(blank=True, null=True)   # por si quieres guardar todo el event

    # Identificadores / tiempos
    tiktok_comment_id = models.CharField(max_length=128, blank=True)  # si en algún punto lo tienes
    tiktok_timestamp = models.DateTimeField(null=True, blank=True)    # timestamp que manda el listener
    received_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tiktok_comments"
        indexes = [
            models.Index(fields=["streamer", "received_at"]),
            models.Index(fields=["tiktok_user_id"]),
        ]

    def __str__(self):
        return f"{self.tiktok_nickname}: {self.text[:30]}"
