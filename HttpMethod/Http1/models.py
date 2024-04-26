from django.db import models

# Create your models here.
class data(models.Model):
    personid = models.CharField(max_length=100)
    lastname = models.CharField(max_length=3)
    firstname = models.CharField(max_length=15)
    address = models.CharField(max_length=255,editable=True)
    city = models.CharField(max_length=255,editable=True)