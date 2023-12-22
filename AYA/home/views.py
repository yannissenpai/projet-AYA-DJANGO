from multiprocessing import context
from django.shortcuts import render
from .models import student, grade
from .form import CreatStudent
from reportlab.pdfgen import canvas
from django.http import HttpResponse


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

def gpdf(request):
    message = ""
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            student_instance = student.objects.get(name=name)
            grades = grade.objects.filter(student=student_instance)
            
            # Création de la réponse HTTP de type PDF
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{name}_grades.pdf"'

            # Création d'un objet canvas pour dessiner le PDF
            p = canvas.Canvas(response)

            # Écriture des données dans le PDF
            y_position = 800
            for g in grades:
                p.drawString(100, y_position, f"Nom de l'étudiant: {g.student.name}, Matière: {g.name.name}, Note: {g.grade}, Date: {g.date}")
                y_position -= 40

            # Finalisation du PDF
            p.showPage()
            p.save()
            return response
        except student.DoesNotExist:
            message = "Utilisateur introuvable"

    # Rendu du template avec un message d'erreur le cas échéant
    return render(request, 'home/gpdf.html', {'message': message})