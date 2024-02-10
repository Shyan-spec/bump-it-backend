from django.db import models
from django.contrib.auth.models import User
from django.db import models
from datetime import date
# Import the User
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=50, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=250, default='')
    
    def __str__(self):
        return f"{self.name}"
    
# Create your models here.
