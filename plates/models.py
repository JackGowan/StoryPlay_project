
# Create your models here.

#import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User - don't have an individual User model now - using djangomodel
from django.contrib.auth import get_user_model

# Create your models here.

class NewPlate(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    # plate_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    room = models.IntegerField(editable=True, blank=True, default=0)
    title = models.CharField(max_length=50, default="")
    setting = models.CharField(max_length=50, default="")
    world = models.CharField(max_length=50, default="")
    genre = models.CharField(max_length=50, default="")
    character = models.CharField(max_length=50, default="")
    created_date = models.DateTimeField(default=timezone.now)
    plate_complete = models.BooleanField(default=False)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

class PlateContent(models.Model):
    plate_id = models.ForeignKey(NewPlate, on_delete=models.CASCADE)
    Plate_position = models.PositiveIntegerField(default=0)
    storytext = models.TextField(default="")
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.storytext[:50] + "..."

    # author
    # drop story text
    # link to integer

# World:
# Fantasy
# Future
# Modern World
# Newyork
# Magical Realism (genre?)
# Warhammer
# Warhammer 40K
# Lord of the rings


