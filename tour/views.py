from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Tour
from datetime import date

from .forms import TourForm

# Create your views here.


def tour_date(request):
    """ A view to show our Tour page """
    tour = Tour.objects.filter(date__gte=date.today()).order_by('date')
    
    context = {
        'tour': tour,
    }

    return render(request, 'tour/tour_dates.html', context)




@login_required
def add_tour_event(request):
    """Add a Tour Event to the Tour page"""
    if not request.user.is_superuser:
        messages.error(request, "No Access! Only site admin can do that.")
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save()
            messages.success(request, 'Successfully added Tour Event!')
            return redirect(reverse('tour'))
        else:
            messages.error(request, 'Failed to add Tour Event. Please ensure the form is valid.')
    else:
        form = TourForm()

    template = 'tour/add_tour_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)