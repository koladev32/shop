from django.db import models


class Shoes(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()