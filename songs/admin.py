from django.contrib import admin
from .models import *


class SongAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_new',
        'album',
        'date_added',
    )


admin.site.register(Song, SongAdmin)
