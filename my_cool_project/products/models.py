from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=128)
    price = models.CharField(null=False, blank=False, max_length=6)
