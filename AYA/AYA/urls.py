from django.contrib import admin
from django.urls import path
from home.views import test, create_student, delete_user, gpdf, create_grade, delete_grade



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test, name ='home'),
    path('gpdf/', gpdf, name='gpdf'),
    path('create-student/', create_student, name ='createstudent'),
    path('delete-student/', delete_user, name ='supprimer-utilisateur'),
    path('create-grade/', create_grade, name ='creategrade'),
    path('delete-grade/', delete_grade, name ='deletegrade'),
    
]
