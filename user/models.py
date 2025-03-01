from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, null=False, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    last_login = models.DateTimeField(default=None, null=True)