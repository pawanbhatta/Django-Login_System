from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.IntegerField()
    status = models.BooleanField(default=False)
