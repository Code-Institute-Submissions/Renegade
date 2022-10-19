from django.contrib import admin
from .models import *


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'town_or_city',
        'country',
    )


admin.site.register(Member, MemberAdmin)
admin.site.register(Genre)
admin.site.register(Instrument)
