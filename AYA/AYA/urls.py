from django.contrib import admin
from django.urls import path
from home.views import test, create_student, delete_user, gpdf 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test, name ='home'),
    path('gpdf/', gpdf, name='gpdf'),
    path('create-student/', create_student, name ='createstudent'),
    path('supprimer-utilisateur/', delete_user, name='supprimer-utilisateur'),
    
]
