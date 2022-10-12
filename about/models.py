from django.db import models
from datetime import datetime
from django_countries.fields import CountryField



class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Instrument(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    birthdate = models.DateField(blank=True, null=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    country = CountryField(blank_label='Country', null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    instrument = models.ManyToManyField(Instrument)
    description = models.TextField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    @property
    def age(self):
        return int((datetime.now().date() - self.birthdate).days / 365.25)
