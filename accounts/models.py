from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

class CreateUser(AbstractUser):
    

    username= None
    email = models.EmailField(unique=True)
    date_joined = models.DateField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
   
    def __str__(self):
        return self.email



class CustomProfile(models.Model):
    user = models.OneToOneField(CreateUser, on_delete=models.CASCADE,primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField()
    Experience=models.CharField(max_length=200)
    collegename=models.CharField(null=True,max_length=200)
    degree=models.CharField(max_length=1000)
    passout_year=models.IntegerField()
    course=models.CharField(max_length=200)
    schoolname=models.CharField(max_length=200)


    def __str__(self):
        return self.user.email
    
