from django.shortcuts import render
from .models import grade

def home(request, *args, **kwargs):
    grades = grade.objects.all()
    contexte = {
    'name':grade.student
    }
   


    return render(request, 'home/index.html', )




"""
def index(request):
    return render(request, 'home/index.html')
    """