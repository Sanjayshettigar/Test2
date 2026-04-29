from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class UpdateGradeForm(forms.Form):
    name = forms.CharField(max_length=100, label="Student Name")
    new_grade = forms.CharField(max_length=2, label="New Grade")