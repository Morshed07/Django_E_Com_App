from django.contrib import admin
from .models import Category,Product,ProductImages,VariationValue,Banner,MyFavicon,MyLogo


# Register your models here.
class ProductImagesAdmin(admin.StackedInline):
    model= ProductImages



class ProductAdmin(admin.ModelAdmin):

    inlines=[ProductImagesAdmin]
    prepopulated_fields={'slug':('name',)}


admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(VariationValue)
admin.site.register(Banner)
admin.site.register(MyLogo)
admin.site.register(MyFavicon)