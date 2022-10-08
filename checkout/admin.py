from django.contrib import admin
from .models import *

# Register your models here.



class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('customer','order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)








# class OrderAdmin(admin.ModelAdmin):
#     readonly_fields = (
#         'customer',
#         'order_number',
#         'full_name',
#         'date',
#         'country',
#         'date',
#     )

# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = (
#         'order',
#         'product',
#         'quantity',
#     )


# admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem, OrderItemAdmin)