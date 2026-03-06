from django.db import models
from django.db.models import IntegerField


# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    discriptions = models.TextField()
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.name


