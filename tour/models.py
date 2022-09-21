from django.db import models

# Create your models here.


class Tour(models.Model):
    name = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
        
    def __str__(self):
        return self.name
