from __future__ import unicode_literals
# from PIL import Image
from django.db import models

# Create your models here.

class information(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField(max_length=500)
    img = models.FileField(upload_to='documents/%Y/%m/%d')

class menu_item(models.Model):
    title = models.CharField(max_length=15)
    price = models.IntegerField()
    menu_include = models.BooleanField(default=False)
    # columns

class slideshow_images(models.Model):
    fileName = models.CharField(max_length=15)
    image_include = models.BooleanField(default=False)
    alt = models.CharField(max_length=100)
    sort = models.IntegerField()
    # columns

class schedule(models.Model):
    url = models.CharField(max_length=36)
    api_key = models.CharField(max_length=36)
    # columns
