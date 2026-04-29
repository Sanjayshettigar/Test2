from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'list_students.html', {'students': students})

def delete_unpaid(request):
    # Delete all students where fee_paid is False
    Student.objects.filter(fee_paid=False).delete()
    return redirect('student_list')