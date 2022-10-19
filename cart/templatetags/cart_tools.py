from django import template

# Customer template tag for calculating subtotal of every item when quantity is updated

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
