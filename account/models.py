from django.db import models

from django.db.models.signals import post_save

from django.dispatch import receiver

from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=100,blank=True,null=True)
    address = models.TextField(max_length=300,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    zipcode = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=14,blank=True,null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def created_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.created(user=instance)

receiver(post_save, sender=User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()