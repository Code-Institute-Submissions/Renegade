from django.shortcuts import render
from .models import Song

# Create your views here.


def song(request):

    song = Song.objects.all()

    context = {
        'song': song,
    }

    return render(request, 'songs/videos.html', {"song": song} )