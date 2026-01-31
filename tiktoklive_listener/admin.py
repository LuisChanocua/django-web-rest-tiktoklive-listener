from django.contrib import admin
from .models import TikTokStreamer, TikTokComment, TikTokListenerConfig

# Register your models here.
@admin.register(TikTokStreamer)
class TikTokStreamerAdmin(admin.ModelAdmin):
    list_display = ("username", "display_name", "is_active", "created_at")
    search_fields = ("username", "display_name")
    list_filter = ("is_active",)

@admin.register(TikTokComment)
class TikTokCommentAdmin(admin.ModelAdmin):
    list_display = ("streamer", "tiktok_user_id", "tiktok_nickname", "text", "received_at")
    search_fields = ("text", "tiktok_user_id", "tiktok_nickname", "tiktok_user_id")
    list_filter = ("streamer",)  
@admin.register(TikTokListenerConfig)
class TikTokListenerConfigAdmin(admin.ModelAdmin):
    list_display = ("enabled", "updated_at")