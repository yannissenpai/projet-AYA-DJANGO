from django.contrib import admin
from django.urls import path
from home.views import test, create_student, delete_student, gpdf



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test, name ='home'),
    path('gpdf/', gpdf, name='gpdf'),
    path('create-student/', create_student, name ='createstudent'),
    path('delete-student/', delete_student, name ='deletetestudent'),
    
]
