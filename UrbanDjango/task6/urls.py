from django.urls import path
from .views import *


urlpatterns = [
    path('', home_view, name='home'),
    path('shop/', shop_view, name='shop'),
    path('cart/', cart_view, name='cart'),
    path('sign_up_django/', sign_up_by_django, name='sign_up_django'),
    path('sign_up_html/', sign_up_by_html, name='sign_up_html'),
    path('create_records/', create_records, name='create_records'),
    path('clear_database/', clear_database, name='clear_database'),
    path('view_objects_with_pagination/', view_objects_with_pagination, name='view_objects_with_pagination'),
]
