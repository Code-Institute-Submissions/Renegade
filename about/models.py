from django.db import models
from datetime import datetime


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
    country = models.CharField(max_length=40, null=False, blank=False)
    genre = models.ForeignKey('Genre', null=True, blank=True, on_delete=models.SET_NULL)
    instrument = models.ForeignKey('Instrument', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(default=False)
    image = models.ImageField(null=True, blank=True)

    @property
    def age(self):
        return int((datetime.now().date() - self.birthdate).days / 365.25)
