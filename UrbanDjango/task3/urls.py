from django.urls import path
from .views import home_view, shop_view, cart_view

urlpatterns = [
    path('', home_view, name='home'),
    path('shop/', shop_view, name='shop'),
    path('cart/', cart_view, name='cart'),
]