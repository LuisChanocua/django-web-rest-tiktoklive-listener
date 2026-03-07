from django.urls import include, path

urlpatterns = [
    path('proxy/', include('lookerstudio_proxy.urls.lookerstudio_proxy_urls')),
]