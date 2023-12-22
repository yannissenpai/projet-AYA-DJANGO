from django.urls import path
from . import views

urlpatterns =  [
    path('', views.index, name='index'),
    path('gpdf/', views.index, name='gpdf'),
    path('create-student/', views.index, name='createS'),
    path('delete-student/', views.index, name='deleteS'),


]