from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.
class Destination(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    
    # author = models.ForeignKey(User, default=None,on_delete=models.CASCADE)

class Employee(models.Model):
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    location = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
  

    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    