from django.urls import path
from ..views.tiktok_comment_views import TikTokCommentInView

urlpatterns = [
    path("comments/", TikTokCommentInView.as_view(), name="tiktok-comments-in"),
]