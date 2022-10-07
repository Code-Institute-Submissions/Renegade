from django.shortcuts import render
from .models import Tour
from datetime import date

# Create your views here.


def tour_date(request):
    """ A view to show our Tour page """
    tour = Tour.objects.filter(date__gte=date.today()).order_by('date')
    
    context = {
        'tour': tour,
    }

    return render(request, 'tour/tour_dates.html', context)
