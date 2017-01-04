from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    desc = models.TextField()
    hexcolor = models.CharField(max_length=5)
