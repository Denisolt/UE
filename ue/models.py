from django.db import models
from colorfield.fields import ColorField
from django.utils import timezone
# Create your models here.
# Mahmoud Saleh, [03.01.17 22:09]
class Event(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    desc = models.TextField()
    color = ColorField(default='#3498db')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
