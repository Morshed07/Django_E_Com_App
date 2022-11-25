from django import template

from order.models import Cart, Order

register = template.Library()

@register.filter
def cart_view(user):
    cart = Cart.objects.filter(user=user, purchased=False)
    if cart.exists():
        return cart
    else:
        return ValueError("You haven't an active cart!")

@register.filter
def cart_total(user):
    order =  Order.objects.filter(user=user, ordered=False)
    if order.exists():
        return order[0].get_total()
    else:
        return 0

@register.filter
def cart_count(user):
    order =  Order.objects.filter(user=user, ordered=False)
    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0