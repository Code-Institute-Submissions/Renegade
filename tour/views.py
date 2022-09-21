from django.shortcuts import render
from .models import Tour

# Create your views here.


def tour_date(request):
    """ A view to show our Tour page """

    tour = Tour.objects.all()

    context = {
        'tour': tour,
    }

    return render(request, 'tour/tour_dates.html', context)
