from django import forms
from .models import student

class CreatStudent(forms.ModelForm):
	class Meta:
	   model= student
	   fields = ('name', 'first_name', 'student_code',)


class DeletStudent(forms.Form):
	student_code = forms.IntegerField(widget=forms.HiddenInput())