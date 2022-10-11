from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import *
from .forms import ProductForm


# Create your views here.


def store(request):
    """ A view to show our Store page, including sorting and search queries """

    products = Product.objects.all()
    query = None
    sort = None
    direction = None


    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('store'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'


    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,

    }

    return render(request, 'store/store.html', context)



def product_info(request, product_id):
    """ A view to show product information """

    product = get_object_or_404(Product, pk=product_id)


    context = {
        'product': product,
    }

    return render(request, 'store/product_info.html', context)



def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'store/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
