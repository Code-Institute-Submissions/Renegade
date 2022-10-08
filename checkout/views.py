from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('store'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Lqm06LjKG7gZcoCUBzKgegbB8Zo5DebYSq91rnW77wiZQ10VjoyiBAml4F3RxaRFVXB7CGT077fWXEbdHw4l5mC0023SEwjXg',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)