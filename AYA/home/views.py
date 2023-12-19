from django.shortcuts import render
from .models import grade

def test(request, *args, **kwargs):
	Grade = grade.objects.get(id=1)
    context = {
    'name':grade.name
    'student':grade.student

    }
    return render(request, 'home/index.html', context )




"""
def index(request):
    return render(request, 'home/index.html')
    """