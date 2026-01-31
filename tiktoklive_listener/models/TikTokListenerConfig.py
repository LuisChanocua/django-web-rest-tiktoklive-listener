# app_tiktok/models.py
from django.db import models

class TikTokListenerConfig(models.Model):
    enabled = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tiktok_listener_config"

    def __str__(self):
        estado = "ON" if self.enabled else "OFF"
        return f"Listener {estado}"

    @classmethod
    def get_solo(cls):
        # Obtiene (o crea) el único registro de config global
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
