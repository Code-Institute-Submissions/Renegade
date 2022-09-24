from django.contrib import admin
from .models import Tour

# Register your models here.


class TourAdmin(admin.ModelAdmin):
    list_display = (
        'location',
        'venue',
        'date',
    )
    ordering = ('date',)


admin.site.register(Tour, TourAdmin)
