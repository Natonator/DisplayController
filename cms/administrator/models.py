from __future__ import unicode_literals

from django.db import models

# Create your models here.
class slideshow_images(models.Model):
    fileName = models.CharField(max_length=15)
    image_include = models.BooleanField(default=False)
    alt = models.CharField(max_length=100)
    # columns

class menu_item(models.Model):
    title = models.CharField(max_length=15)
    price = models.IntegerField()
    menu_include = models.BooleanField(default=False)
    # columns

class schedule(models.Model):
    url = models.CharField(max_length=36)
    api_key = models.CharField(max_length=36)
    # columns
