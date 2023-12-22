from django import forms
from .models import student


class DeleteUserForm(forms.Form):
    username = forms.CharField(label='Nom d’utilisateur', max_length=100)
	
class CreatStudent(forms.ModelForm):
	class Meta:
	   model= student
	   fields = ('name', 'first_name', 'student_code',)


