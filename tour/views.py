from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Tour
from datetime import date
from .forms import TourForm


# TOUR EVENTS
def tour_date(request):
    """ A view to show our Tour page """
    tour = Tour.objects.filter(date__gte=date.today()).order_by('date')

    context = {
        'tour': tour,
    }

    return render(request, 'tour/tour_dates.html', context)


# ADD TOUR EVENT
@login_required
def add_tour_event(request):
    """Add a Tour Event to the Tour page"""
    if not request.user.is_superuser:
        messages.error(request, "No Access! Only site admin can do that.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
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


# ADD TOUR EVENT
@login_required
def edit_tour_event(request, tour_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'No access! Only site admin can do that.')
        return redirect(reverse('tour'))

    tour = get_object_or_404(Tour, pk=tour_id)
    if request.method == 'POST':
        form = TourForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated tour event!')
            return redirect(reverse('tour'))
        else:
            messages.error(request, 'Failed to update tour event. Please ensure the form is valid.')
    else:
        form = TourForm(instance=tour)
        messages.info(request, f'You are editing {tour.venue}')

    template = 'tour/edit_tour_event.html'
    context = {
        'form': form,
        'tour': tour,
    }
    return render(request, template, context)


# DELETE TOUR EVENT
@login_required
def delete_tour_event(request, tour_id):
    """ Delete a tour event from the Tour """
    if not request.user.is_superuser:
        messages.error(request, 'No access! Only tour admin can do that.')
        return redirect(reverse('tour'))

    tour = get_object_or_404(Tour, pk=tour_id)
    tour.delete()
    messages.success(request, 'Tour event deleted!')
    return redirect(reverse('tour'))
