from django.urls import path
from . import views

urlpatterns =  [
    path('', views.index, name='index'),
    path('create-student/', views.index, name='createS'),
    path('delete-student/', views.index, name='deleteS'),


]