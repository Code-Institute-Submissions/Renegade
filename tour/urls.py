from django.urls import path
from . import views

urlpatterns = [
    path('', views.tour_date, name='tour'),
    path('edit/<int:tour_id>/', views.edit_tour_event, name='edit_tour_event'),
    path('add/', views.add_tour_event, name='add_tour_event'),
    path('delete/<int:tour_id>/', views.delete_tour_event, name='delete_tour_event'),

]