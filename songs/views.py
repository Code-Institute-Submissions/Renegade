from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Song
from .forms import SongForm


def song(request):

    song = Song.objects.all()

    context = {
        'song': song,
    }

    return render(request, 'songs/videos.html', {"song": song} )



@login_required
def add_song(request):
    """Add a Song to Videos page"""
    if not request.user.is_superuser:
        messages.error(request, "No Access! Only site admin can do that.")
        return redirect(reverse('videos'))
    
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Song successfully added!')
            return redirect(reverse('videos'))
        else:
            messages.error(request, 'Failed to add the Song. Please ensure the form is valid.')
    else:
        form = SongForm()

    template = 'songs/add_song.html'
    context = {
        'form': form,
    }
    return render(request, template, context)



@login_required
def edit_song(request, song_id):
    """ Edit a song in the videos section """
    if not request.user.is_superuser:
        messages.error(request, 'No access! Only a site admin can do that.')
        return redirect(reverse('videos'))

    song = get_object_or_404(Song, pk=song_id)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated song!')
            return redirect(reverse('videos', args=[song.id]))
        else:
            messages.error(request, 'Failed to update the song details. Please ensure the form is valid.')
    else:
        form = SongForm(instance=song)
        messages.info(request, f'You are editing {song.name} from {song.album} album.')

    template = 'songs/edit_song.html'
    context = {
        'form': form,
        'song': song,
    }
    return render(request, template, context)




@login_required
def delete_song(request, song_id):
    """ Delete a song from page videos """
    if not request.user.is_superuser:
        messages.error(request, 'No access! Only site admin can do that.')
        return redirect(reverse('song'))

    song = get_object_or_404(Song, pk=song_id)
    song.delete()
    messages.success(request, 'Song deleted!')
    return redirect(reverse('videos'))