from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    bio = models.TextField(blank=True, max_length=255)
    private = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username