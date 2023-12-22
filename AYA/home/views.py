from django.shortcuts import render
from .models import student
from .form import CreatStudent

def test(request, *args, **kwargs):
    students = student.objects.all()
    context = {
    'students': students,
    }
    return render(request, 'home/detail.html', context)

def createS(request):
    form = CreatStudent(request.POST or None)
    message = ' '
    if form.is_valid():
        form.save()
        form = CreatStudent()
        message = '+1 Student added'


    return render(request, 'home/detailcreateS.html', {'form':form, 'message':message,})




"""
def index(request):
    return render(request, 'home/index.html')
    """