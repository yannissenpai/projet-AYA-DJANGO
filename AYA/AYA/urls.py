from django.contrib import admin
from django.urls import path
from home.views import test, createS, gpdf



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test, name ='home'),
    path('create-student/', createS, name ='createstudent'),
    path('gpdf/', gpdf, name='gpdf'),

]
