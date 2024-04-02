from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/cart', views.add_to_cart, name='add_to_cart'),
]