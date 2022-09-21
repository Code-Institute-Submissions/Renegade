from django.contrib import admin
from .models import Tour

# Register your models here.


class TourAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'date',
    )
    ordering = ('-date',)


admin.site.register(Tour, TourAdmin)
