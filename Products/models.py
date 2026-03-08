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



from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title