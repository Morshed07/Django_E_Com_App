from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, blank=False,null=False)
    image = models.ImageField(upload_to='category_images',blank=True,null=True)
    parent = models.ForeignKey(self, related_name='children', on_delete=models.CASCADE,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-created']
        verbose_name_plural="Categories"

class Product(models.Model):
    name=models.CharField(max_length=250, blank=False,null=False)
    category