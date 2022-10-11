from django.urls import path
from . import views

urlpatterns = [
    path('', views.tour_date, name='tour'),
    path('add/', views.add_tour_event, name='add_tour_event'),

]