from django.db import models
from django.contrib.auth.models import AbstractUser 
from .managers import CustomUserManager




class CustomUser(AbstractUser):
    username = None
    phone = models.CharField(max_length=100, unique=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['phone']

    groups = models.ManyToManyField(
        to='auth.Group',
        related_name='customuser_set'
    )
    
    user_permissions = models.ManyToManyField(
        to='auth.Permission',
        related_name='customuser_set'
    )

