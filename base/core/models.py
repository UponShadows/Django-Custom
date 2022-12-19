from django.db import models
from .manager import UserManager

# Create your models here.
class CustomUser(models.Model):
    objects = UserManager() 
    pass