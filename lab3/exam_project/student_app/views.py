from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def grade_list(request):
    students = Student.objects.filter(grade='O')
    return render(request, 'list_students.html', {'students': students})