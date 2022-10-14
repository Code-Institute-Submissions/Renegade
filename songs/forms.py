from django import forms
from .models import Song


class SongForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder':'Song Name'}))
    album = forms.CharField(label='Album', widget=forms.TextInput(attrs={'placeholder':'Album Name'}))
    is_new = forms.BooleanField(label='New Song?', required=False)
    url = forms.URLField(label='URL', widget=forms.TextInput(attrs={'placeholder':'Video URL'}))

    class Meta:
        model = Song
        fields = ['name', 'album', 'is_new', 'url']
