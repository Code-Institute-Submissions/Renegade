from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    album = models.CharField(max_length=50, null=False, blank=False)
    is_new = models.BooleanField(default=False, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=250)
    

    def __str__(self):
        return self.name
