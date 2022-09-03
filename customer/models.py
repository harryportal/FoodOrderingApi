from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    date_created = models.DateField(auto_now_add=True)
    email = models.EmailField(unique=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=100,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'