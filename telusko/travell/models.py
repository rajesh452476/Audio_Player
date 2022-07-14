from django.db import models

# Create your models here.

class Song(models.Model):
    movie = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    img   = models.ImageField(upload_to='images/')
    audio  = models.FileField(upload_to='media')

def __str__(self):
    return self.title