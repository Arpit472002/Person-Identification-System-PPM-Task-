from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class MyUser(AbstractUser):
    user_id   = models.AutoField(primary_key=True)
    username=models.CharField(max_length=200,unique=True)
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]
    
    def __str__(self):
        return self.username

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        token=Token.objects.create(user = instance)