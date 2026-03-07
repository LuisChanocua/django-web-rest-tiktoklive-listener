from django.urls import path
from lookerstudio_proxy.views.views import daily_products_proxy, daily_users_proxy

urlpatterns = [
    path('products/daily-products/', daily_products_proxy, name='proxy-products-daily-products'), 
    path('users/daily-users/', daily_users_proxy, name='proxy-users-daily-users'), 
]