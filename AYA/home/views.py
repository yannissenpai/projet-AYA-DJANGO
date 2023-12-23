from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from django.http import HttpResponse
from .models import student, grade, subject
from django.shortcuts import render, redirect
from multiprocessing import context
from .form import CreatStudent, CreatGrade
from django.contrib import messages



""" Page d'accueil """
def test(request, *args, **kwargs):
    students = student.objects.all()
    context = {
    'students': students,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            student_instance = student.objects.get(name=name)
            grades = grade.objects.filter(student=student_instance)
            context['student_instance'] = student_instance
            context['grades'] = grades
        except student.DoesNotExist:
            message = "Utilisateur introuvable"
            context['message'] = message
    return render(request, 'home/detail.html', context)



""" Création de PDF """
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

            # Préparation des données pour le premier tableau
            data = [["Nom de l'étudiant", "Matière", "Note", "Date"]]
            total_grade = 0
            for g in grades:
                data.append([g.student.name, g.name, g.grade, g.date])
                total_grade += g.grade

            # Calcul de la moyenne générale
            average_grade = total_grade / len(grades) if grades else 0

            # Création et ajout du premier tableau
            table = Table(data)
            table_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
                ('ALIGN',(0,0),(-1,-1),'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND',(0,1),(-1,-1),colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ])
            table.setStyle(table_style)
            elements.append(table)

            # Préparation des données pour le second tableau (moyenne générale)
            avg_data = [["Moyenne Générale", "{:.2f}".format(average_grade)]]
            avg_table = Table(avg_data, [200, 50])  # Ajustez les dimensions selon vos besoins
            avg_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                ('ALIGN',(0,0),(-1,-1),'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ])
            avg_table.setStyle(avg_style)
            elements.append(avg_table)

            # Construction du PDF
            doc.build(elements)
            return response
        except student.DoesNotExist:
            message = "Student not found"

    return render(request, 'home/gpdf.html', {'message': message})



""" Création student"""
def create_student(request):
    form = CreatStudent(request.POST or None)
    message = ' '
    if form.is_valid():
        form.save()
        form = CreatStudent()
        message = '+1 Student added'


    return render(request, 'home/detailcreateS.html', {'form':form, 'message':message,})



""" Suppression student"""
def delete_user(request):
    if request.method == 'POST':
        student_name = request.POST.get('name')
        try:
            user = student.objects.get(name=student_name)
            # Il n'est pas nécessaire de filtrer les instances de student si vous supprimez un seul étudiant
            grade.objects.filter(student=user).delete()  # Supprime les grades de l'étudiant
            user.delete()
            messages.success(request, 'The student has been deleted.')
        except student.DoesNotExist:
            messages.error(request, 'Student not found.')
        return redirect('supprimer-utilisateur')  # Assurez-vous que c'est la bonne URL de redirection

    return render(request, 'home/deleteS.html')



""" Création grade"""
def create_grade(request):
    form = CreatGrade(request.POST or None)
    message = ' '
    if form.is_valid():
        form.save()
        form = CreatGrade()
        message = '+1 Grade added'


    return render(request, 'home/detailcreateG.html', {'form':form, 'message':message,})



""" Suppression student"""
def delete_grade(request):
    if request.method == 'POST':
        student_name = request.POST.get('name')
        try:
            user = student.objects.get(name=student_name)
            # Il n'est pas nécessaire de filtrer les instances de student si vous supprimez un seul étudiant
            grade.objects.filter(student=user).delete()  # Supprime les grades de l'étudiant
            user.delete()
            messages.success(request, 'The grade has been deleted.')
        except student.DoesNotExist:
            messages.error(request, 'Grade not found.')
        return redirect('supprimer-utilisateur')  # Assurez-vous que c'est la bonne URL de redirection

    return render(request, 'home/deleteG.html')