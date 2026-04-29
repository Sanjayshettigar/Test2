from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('amazon_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def amazon_list(request):
    students = Student.objects.filter(company_name='Amazon')
    return render(request, 'amazon_students.html', {'students': students})