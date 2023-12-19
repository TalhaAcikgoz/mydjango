from django.db import models

# Create your models here.

class myModel(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)