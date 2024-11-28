from django.urls import path
from .views import function_based_view, ClassBasedView

urlpatterns = [
    path('function-view/', function_based_view, name='function_view'),
    path('class-view/', ClassBasedView.as_view(), name='class_view'),
]