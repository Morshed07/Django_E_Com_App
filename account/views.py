from django.shortcuts import render,HttpResponse
from .forms import RegistrationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate
# Create your views here.


def Register(request):
    if request.user.is_authenticated:
        return HttpResponse('u r authenticated!')
    else:
        form = RegistrationForm()
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                
                return HttpResponse('ur account has been cretaed')
    context={
        "form": form
    }
    return render(request, 'accounts/register.html',context)

def CustomerLogin(request):
    if request.user.is_authenticated:
        return HttpResponse('u r logged in')
    else:
        if request.method =="POST":
            username= request.POST.get('username')
            password= request.POST.get('password')
            customer = authenticate(request,username=username,password=password)
            if customer is not None:
                login(request, customer)
                return HttpResponse('u r logged in succesfully')
            else:
                return HttpResponse('404')
    return render(request, 'accounts/login.html')