from django.shortcuts import render, redirect
from .models import Faculty
from .forms import FacultyForm

def add_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cse_prof_list')
    else:
        form = FacultyForm()
    return render(request, 'add_faculty.html', {'form': form})

def cse_prof_list(request):
    faculty = Faculty.objects.filter(branch='CSE', title='Professor')
    return render(request, 'list_faculty.html', {'faculty': faculty})