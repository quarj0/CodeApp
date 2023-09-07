from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    staff_id = models.CharField(max_length=10, unique=True)
    department = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    
