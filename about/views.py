from django.shortcuts import render
from .models import *

# Create your views here.


def about(request):
    """ A view to show members of the band """

    member = Member.objects.all()


    context = {
        'member': member,
    }

    return render(request, 'about/about.html', context)
