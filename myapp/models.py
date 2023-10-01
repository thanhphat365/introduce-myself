from django.db import models
from datetime import datetime

# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=20)
    Images =models.ImageField(upload_to = '')
    age = models.CharField(max_length=3)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
#About
class About(models.Model):
    heding = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile = models.ImageField(upload_to='')
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.career