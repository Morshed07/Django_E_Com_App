from django import forms
from .models import BillingAddress
from order.models import Order





class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['user','first_name','last_name','address1','address2','country','city','zipcode','phone_number']


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method',]