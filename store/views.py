from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product,ProductImages,Banner


# Create your views here.
class HomeListView(ListView):
    model= Product
    template_name= "store/index.html"
    context_object_name= "products"


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["banners"] = Banner.objects.filter(is_active=True).order_by('-id')[0:3]
        return context
    


class ProductDetailView(DetailView):
    model=Product
    template_name='store/product.html'
    context_object_name= 'item'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['product_pics']= ProductImages.objects.filter(product=self.object.id)

        return context