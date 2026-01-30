# tiktoklive_listener/urls/__init__.py
from django.urls import include, path

urlpatterns = [
    path("tiktok-live/", include("tiktoklive_listener.urls.tiktok_live_urls")),
]