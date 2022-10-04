from django.shortcuts import render
from store.models import *

# Create your views here.


def view_cart(request):

    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitem_set.all()
    # else:
    #     items = []

    # context = {'items':items}
    return render(request, 'cart/cart.html')