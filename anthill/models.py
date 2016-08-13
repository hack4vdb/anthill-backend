from __future__ import unicode_literals

import uuid
from django.contrib.gis.db import models

# Create your models here.


#Datenfelder fuer Import CSV: Anrede (Herr, Frau, Keine Angabe), Vornamen (Textfeld),
# Nachname (Textfeld), E-Mail Adresse, PLZ (4-digit), Strasse, Hausnummer

#Land, PLZ, Ort, Strasse, Hausnummer, Tuernummer, Anrede, Vorname, Nachname,
# E-Mail Adresse, Produktbedarf (Paket mit 500 Flyern)

class Activist(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    anrede = models.CharField(max_length=100, null=True, blank=True) #Anrede (Herr, Frau, Keine Angabe)
    first_name = models.CharField(max_length=300, null=True, blank=True)
    last_name = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField()
    postalcode = models.IntegerField() #PLZ (4-digit)
    municipal = models.CharField(max_length=500, null=True, blank=True) #Ort
    street = models.CharField(max_length=500, null=True, blank=True)
    house_number = models.CharField(max_length=100, null=True, blank=True)
    coordinate = models.PointField(null=True, blank=True)
    # todo:
    # - hash as link to user

    def __str__(self):
        return '{} ({})'.format(self.email, self.postalcode)


class Meetup(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=1000)
    datetime = models.DateTimeField()
    postalcode = models.IntegerField() #PLZ (4-digit)
    municipal = models.CharField(max_length=500) #Ort
    street = models.CharField(max_length=500)
    house_number = models.CharField(max_length=100)
    coordinate = models.PointField()
    activist = models.ManyToManyField(Activist, null=True, blank=True)

    def __str__(self):
        return self.title
