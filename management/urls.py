from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.management, name='management'),
    path('store/', include('store.urls')),
    path('tour/', include('tour.urls')),
    path('about/', include('about.urls')),
    path('videos/', include('songs.urls')),
]