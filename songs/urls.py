from django.urls import path
from . import views

urlpatterns = [
    path('', views.song, name='videos'),
    path('edit/<int:song_id>/', views.edit_song, name='edit_song'),
    path('add/', views.add_song, name='add_song'),
    path('delete/<int:song_id>/', views.delete_song, name='delete_song'),

]