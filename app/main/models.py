from django.db import models


# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=150)
    disc = models.TextField(max_length=255)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
