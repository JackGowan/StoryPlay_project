from django.db import models

# Create your models here.

# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

#using django's internal model 'abstract user' - adding on an age field - e.g. a sub-class
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

