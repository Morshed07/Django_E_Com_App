from django.db import models

from django.dispatch import receiver

from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASECADE, related_name="profile")
    full_name = models.CharField(max_length=100,blank=True,null=True)
    address = models.TextField(max_length=300,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    full_name = models.CharField(max_length=100,blank=True,null=True)
    full_name = models.CharField(max_length=100,blank=True,null=True)
    