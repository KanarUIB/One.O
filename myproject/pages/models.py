from django.db import models

# Create your models here.

class Kunde(models.Model):
    mandant = models.CharField(max_length=50)
    software = models.ForeignKey("Software", on_delete=models.CASCADE)


class Software(models.Model):
    software = models.CharField(max_length=50)