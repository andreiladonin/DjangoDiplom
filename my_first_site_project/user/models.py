from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    date_birthday = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="users_images", blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    sex = models.CharField(max_length=12, null=True, blank=True)


