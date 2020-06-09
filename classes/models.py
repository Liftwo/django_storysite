from django.db import models
from django.utils import timezone
# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    yrsold = models.DecimalField(max_digits=3, decimal_places=0)
    skills = models.CharField(max_length=50, blank=True)


class Photo(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    story = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
