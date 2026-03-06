from django.urls import path
from ..views.tiktok_comment_views import TikTokCommentInView
from ..views.tiktok_live_view import ActiveListenerStreamersView, ListenerToggleView, daily_products_proxy

urlpatterns = [
    path("comments/", TikTokCommentInView.as_view(), name="tiktok-comments-in"),
    path("active-streamers/", ActiveListenerStreamersView.as_view(), name="tiktok-active-streamers"),
    path("listener/toggle/", ListenerToggleView.as_view(), name="tiktok-listener-toggle"),
    path("proxy/daily-products/", daily_products_proxy, name="proxy-daily-products"),
]