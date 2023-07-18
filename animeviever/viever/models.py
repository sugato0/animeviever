from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    series = models.IntegerField()
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    
    description = models.TextField()

    def __str__(self):
        return self.title
    

