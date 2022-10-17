from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

def home(request):
    return render(request, "store\index.html")