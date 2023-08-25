from django.shortcuts import render,HttpResponse,redirect
from .forms import RegistrationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate
from order.models import Cart,Order
from payment.models import BillingAddress
from account.models import Profile
from payment.forms import BillingAddressForm
from account.forms import ProfileForm
from django.views.generic import TemplateView
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

class ProfileView(TemplateView):
    def get(self,request,*args, **kwargs):
        orders =  Order.objects.filter(user=request.user,ordered=True)
        billingaddress = BillingAddress.objects.get(user=request.user)
        billingaddress_form = BillingAddressForm(instance=billingaddress)

        profile_obj=Profile.objects.get(user=request.user)
        profileform = ProfileForm(instance=profile_obj)

        context = {
            'orders' : orders,
            'billingaddress': billingaddress_form,
            'profileform': profileform
        }
        return render(request,'accounts/dashboard.html',context)
    
    def post(self,request,*args, **kwargs):
        if request.method =='post' or request.method == 'POST':
            billingaddress = BillingAddress.objects.get(user=request.user)

            billigaddress_form= BillingAddressForm(request.POST,instance=billingaddress)
            profile_obj=Profile.objects.get(user=request.user)
            profileform = ProfileForm(request.POST,instance=profile_obj)
            if billigaddress_form.is_valid() or profileform.is_valid():
                billigaddress_form.save()
                profileform.save()
                return redirect('account:profile')