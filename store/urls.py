from django.urls import path
from . import views

from django.shortcuts import render
app_name= 'store'
urlpatterns = [
    path('',views.HomeListView.as_view(),name="home"),
    # path('product/<slug:slug>/',views.ProductDetailView.as_view(),name="product_details"),
    path('product/<int:pk>/',views.product_details,name="product_details"),
]