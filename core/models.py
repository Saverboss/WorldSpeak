from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')), null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username