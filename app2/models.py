from django.db import models

# Create your models here.
class Formsdata(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)

