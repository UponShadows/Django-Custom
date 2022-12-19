from django.db import models
from .manager import UserManager

# Create your models here.
class CustomUser(models.Model):
    username = None # Removes username field so u login with email 
    
    
    
    
    objects = UserManager() 
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    pass