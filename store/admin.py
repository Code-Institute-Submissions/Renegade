from django.contrib import admin
from .models import *

# Register your models here.



class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'email',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'digital',
        'image',
    )
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'date_ordered',
        'complete',
        'transaction_id',
    )

class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'order',
        'quantity',
    )


class ShippingAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'order',
        'town_or_city',
        'postcode',
        'country',
        'date',
    )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAdmin)