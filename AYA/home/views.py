from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from django.http import HttpResponse
from .models import student, grade  # Assurez-vous que les modèles sont correctement importés
from django.shortcuts import render

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

            # Création d'un document PDF
            doc = SimpleDocTemplate(response, pagesize=letter)
            elements = []

            # Préparation des données pour le tableau
            data = [["Nom de l'étudiant", "Matière", "Note", "Date"]]
            for g in grades:
                data.append([g.student.name, g.name.name, g.grade, g.date])

            # Création du tableau
            table = Table(data)

            # Style du tableau (ajustez selon vos besoins)
            style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
                ('ALIGN',(0,0),(-1,-1),'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND',(0,1),(-1,-1),colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ])
            table.setStyle(style)

            # Ajout du tableau au document
            elements.append(table)

            # Construction du PDF
            doc.build(elements)
            return response
        except student.DoesNotExist:
            message = "Utilisateur introuvable"

    # Rendu du template avec un message d'erreur le cas échéant
    return render(request, 'home/gpdf.html', {'message': message})