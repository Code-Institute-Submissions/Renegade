from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


def management(request):
    """ A view to show our Management page """

    return render(request, 'management/management.html')
