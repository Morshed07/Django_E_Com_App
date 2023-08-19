from django.urls import path
from . import views


app_name= 'store'
urlpatterns = [
    path('',views.HomeListView.as_view(),name="home"),
    path('product/<slug:slug>/',views.ProductDetailView.as_view(),name="product_details"),
]