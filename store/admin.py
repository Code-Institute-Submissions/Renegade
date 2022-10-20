from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'name',
        'category',
        'sku',
        'price',
        'digital',
        'image',
    )
    summernote_fields = ('description')
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
