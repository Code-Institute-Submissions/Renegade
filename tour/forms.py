from django import forms
from django.forms import ModelForm
from .models import Tour
from django.contrib.admin import widgets


class DateInput(forms.DateInput):
    input_type = 'date'

class TourForm(forms.ModelForm):
    location = forms.CharField(label='Location', widget=forms.TextInput(attrs={'placeholder':'City, Country/State'}))
    venue = forms.CharField(label='Venue', widget=forms.TextInput(attrs={'placeholder':'Venue Name'}))
    date = forms.DateField(widget=DateInput())

    class Meta:
        model = Tour
        fields = ['location', 'venue', 'date']
