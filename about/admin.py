from django.contrib import admin
from .models import *

# Register your models here.



class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'instrument',
    )



admin.site.register(Member, MemberAdmin)
admin.site.register(Genre)
admin.site.register(Instrument)