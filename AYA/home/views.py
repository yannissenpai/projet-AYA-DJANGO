from django.shortcuts import render,get_object_or_404, redirect
from .models import student
from .form import CreatStudent, DeletStudent

def test(request, *args, **kwargs):
    students = student.objects.all()
    context = {
    'students': students,
    }
    return render(request, 'home/detail.html', context)





""" Création et Suppression """

def create_student(request):
    form = CreatStudent(request.POST or None)
    message = ' '
    if form.is_valid():
        form.save()
        form = CreatStudent()
        message = '+1 Student added'


    return render(request, 'home/detailcreateS.html', {'form':form, 'message':message,})


def delete_student(request, *args, **kwargs):
    delstudent = get_object_or_404(student, student_code=student_code)

    if request.method == 'POST':
        form = DeletStudent(request.POST)
        if form.is_valid() and form.cleaned_data['student_code'] == student_code:
            # Supprimez l'étudiant
            delstudent.delete()
            return redirect('student')  # Remplacez 'liste_etudiants' par le nom de votre vue de liste d'étudiants
    else:
        form = DeletStudent(initial={'student_code': student_code})

    return render(request, 'home/detaildeleteS.html', {'form': form, 'student': delstudent})


"""
def index(request):
    return render(request, 'home/index.html')
    """