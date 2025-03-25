from django.db import models
from django.contrib.auth.models import AbstractUser 
from .managers import CustomUserManager




class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(unique=True, max_length=13, default='default_num')
    email = models.EmailField(unique=True, null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    objects = CustomUserManager()

    groups = models.ManyToManyField(
        to='auth.Group',
        related_name='customuser_set'
    )

    user_permissions = models.ManyToManyField(
        to='auth.Permission',
        related_name='customuser_set'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

