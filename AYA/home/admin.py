from django.contrib import admin
from .models import student
from .models import subject
from .models import grade

class Adminstudent(admin.ModelAdmin):
    list_display = ('name', 'first_name', 'student_code')

    

class Adminsubject(admin.ModelAdmin):
    list_display = ('name', 'subject_code')

    

class Admingrade(admin.ModelAdmin):
    list_display = ('name', 'student', 'grade', 'date')

    


admin.site.register(student, Adminstudent)
admin.site.register(subject, Adminsubject)
admin.site.register(grade, Admingrade)
