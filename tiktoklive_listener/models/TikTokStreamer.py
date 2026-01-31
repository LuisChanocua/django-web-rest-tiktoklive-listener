# app_tiktok/models.py
from django.db import models

class TikTokStreamer(models.Model):
    username = models.CharField(max_length=64, unique=True)  # sin @
    display_name = models.CharField(max_length=128, blank=True)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    should_listen = models.BooleanField(default=False)
    
    class Meta:
        db_table = "tiktok_streamers"

    def __str__(self):
        return f"@{self.username}"
