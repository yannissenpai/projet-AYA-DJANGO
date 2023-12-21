from django.shortcuts import render
from .models import student

def test(request, *args, **kwargs):
    students = student.objects.all()
    context = {
    'students': students,
    }
    return render(request, 'home/detail.html', context)




"""
def index(request):
    return render(request, 'home/index.html')
    """