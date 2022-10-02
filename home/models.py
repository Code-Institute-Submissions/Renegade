from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=250)

    def __str__(self):
        return self.name

