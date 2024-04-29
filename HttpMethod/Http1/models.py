from django.db import models
from django.urls import reverse

# Create your models here.
class data(models.Model):
    personid = models.CharField(max_length=3)
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    address = models.CharField(max_length=255,editable=True)
    city = models.CharField(max_length=255,editable=True)

    def get_absolute_url(self):
        return reverse("data_delete",kwargs={"id":self.id})