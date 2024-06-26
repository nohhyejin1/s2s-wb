from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('health', views.health, name='health'),
    path('add/cart', views.add_to_cart, name='add_to_cart'),
    path('cart', views.get_cart, name='get_cart'),
]