from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import *

# Create your views here.


def store(request):
    """ A view to show our Store page, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('store'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            store = store.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'store/store.html', context)



def product_info(request, product_id):
    """ A view to show product information """

    product = get_object_or_404(Product, pk=product_id)


    context = {
        'product': product,
    }

    return render(request, 'store/product_info.html', context)
