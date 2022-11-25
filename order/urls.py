from django.urls import path
from . import views


app_name ='order'
urlpatterns = [
    path('add-to-cart/<int:pk>/',views.add_to_cart, name='add-to-cart'),
]