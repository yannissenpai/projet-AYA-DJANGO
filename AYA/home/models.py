from django.db import models

class student(models.Model):
	name = models.CharField(max_length=150)
	first_name = models.CharField(max_length=150)
	student_code = models.CharField(max_length=150, unique=True)

	def __str__(self):
		return self.name
	

class subject(models.Model):
	name = models.CharField(max_length=150)
	subject_code = models.CharField(max_length=150, unique=True)

	def __str__(self):
		return self.name

class grade(models.Model):
	name = models.ForeignKey(subject, on_delete=models.CASCADE)
	student = models.ForeignKey(student, on_delete=models.CASCADE)
	grade = models.DecimalField(max_digits=3, decimal_places=1)
	date = models.DateField()

	


	
	"""
	Pour chaque modif de ma table ou classe faire:
	python manage.py makemigrations
	python manage.py migrate
	"""