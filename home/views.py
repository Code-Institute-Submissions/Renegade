from django.shortcuts import render
from tour.models import Tour
from songs.models import Song

# Create your views here.


def index(request):
    tour = Tour.objects.all()
    song = Song.objects.all()
    return render(request, 'home/index.html', {"tour": tour, "song": song})

