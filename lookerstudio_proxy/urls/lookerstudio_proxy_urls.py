from django.urls import path
from lookerstudio_proxy.views.views import daily_products_proxy

urlpatterns = [
    path('products/daily-products/', daily_products_proxy, name='proxy-products-daily-products'), 
]