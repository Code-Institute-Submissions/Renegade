from django.db import models


class Tour(models.Model):
    """
    Tour model for adding or editing tour events for Tour page
    """
    location = models.CharField(max_length=200, null=True)
    venue = models.CharField(max_length=100, null=True)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return self.location
