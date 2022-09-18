from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def store(request):
    """ A view to show our Store page, including sorting and search queries """

    store = Product.objects.all()


    context = {
        'store': store,
    }

    return render(request, 'store/store.html', context)



def product_info(request, product_id):
    """ A view to show product information """

    product = get_object_or_404(Product, pk=product_id)


    context = {
        'product': product,
    }

    return render(request, 'store/product_info.html', context)
