from django.shortcuts import render
from tour.models import Tour

# Create your views here.


def index(request):
    tour = Tour.objects.all()
    return render(request, 'home/index.html', {"tour": tour})

