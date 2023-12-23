from django import forms
from .models import student, grade

class CreatStudent(forms.ModelForm):
	class Meta:
	   model= student
	   fields = ('name', 'first_name', 'student_code',)


class DeletStudent(forms.Form):
	student_code = forms.IntegerField(widget=forms.HiddenInput())


class CreatGrade(forms.ModelForm):
	class Meta:
	   model= grade
	   fields = ('name', 'student', 'grade', 'date')


class DeletStudent(forms.Form):
	garde_code = forms.IntegerField(widget=forms.HiddenInput())