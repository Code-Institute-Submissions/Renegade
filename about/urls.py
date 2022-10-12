from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('<int:member_id>/', views.member_info, name='member_info'),
    path('edit/<int:member_id>/', views.edit_member, name='edit_member'),
    path('add/', views.add_member, name='add_member'),
    path('delete/<int:member_id>/', views.delete_member, name='delete_member'),
]