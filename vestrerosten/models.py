from django.db import models

# Create your models here.

class Underskrifter(models.Model):
    navn = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    kommentar = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.navn+' '+self.adresse
