from django.shortcuts import render
from tour.models import Tour
from songs.models import Song
from datetime import date

# Create your views here.


def index(request):
    tour = Tour.objects.filter(date__gte=date.today()).order_by('date')
    song = Song.objects.all()
    return render(request, 'home/index.html', {"tour": tour, "song": song})

