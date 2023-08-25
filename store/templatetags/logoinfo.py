from django  import template
from store.models import MyFavicon,MyLogo


register = template.Library()

@register.filter
def logo(request):
    if request:
        logo = MyLogo.objects.filter(is_active=True).order_by('-id').first()
        return logo.image.url
    
    else:
        logo = MyLogo.objects.filter(is_active=True).order_by('-id').first()
        return logo.image.url
    