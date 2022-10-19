from django.contrib import admin
from .models import *


class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_phone_number',
        'default_town_or_city',
        'default_postcode',
        'default_country',
    )


admin.site.register(UserAccount, UserAccountAdmin)
