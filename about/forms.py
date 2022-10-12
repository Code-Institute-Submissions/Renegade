from django import forms
from django.forms import ModelForm

from .models import *
from store.widgets import CustomClearableFileInput


class DateInput(forms.DateInput):
    input_type = 'date'


class GenreField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, genre):
        return "%s" % genre.name

class InstrumentField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, instrument):
        return "%s" % instrument.name



class MemberForm(forms.ModelForm):
    name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'placeholder':'Full Name'}))
    birthdate = forms.DateField(widget=DateInput())
    town_or_city = forms.CharField(label='Town/City', widget=forms.TextInput(attrs={'placeholder':'Town or City'}))
    genre = GenreField(label='Genre', queryset=Genre.objects.all(),widget=forms.CheckboxSelectMultiple)
    instrument = InstrumentField(label='Role', queryset=Instrument.objects.all(),widget=forms.CheckboxSelectMultiple)
    description = forms.CharField(label='Member Description', widget=forms.Textarea(attrs={'placeholder': 'Write something about the member...'}))
    image = forms.ImageField(label='Member Image', required=True, widget=CustomClearableFileInput)

    class Meta:
        model = Member
        fields = ['name', 'birthdate', 'town_or_city', 'country', 'genre', 'instrument','description', 'image']
