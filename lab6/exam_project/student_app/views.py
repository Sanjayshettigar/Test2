from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm, UpdateGradeForm

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('update_grade')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def update_grade(request):
    message = ""
    students = Student.objects.all()
    if request.method == 'POST':
        form = UpdateGradeForm(request.POST)
        if form.is_valid():
            target_name = form.cleaned_data['name']
            new_grade = form.cleaned_data['new_grade']
            updated = Student.objects.filter(name__iexact=target_name).update(grade=new_grade)
            if updated:
                message = f"✅ Grade updated to {new_grade} for {target_name}"
            else:
                message = "❌ Student not found"
            students = Student.objects.all()
    else:
        form = UpdateGradeForm()
    return render(request, 'update_grade.html', {'form': form, 'message': message, 'students': students})