from django.urls import path
from . import views

urlpatterns = [
    path('', views.tour_date, name='tour'),
]