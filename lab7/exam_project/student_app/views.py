from django.shortcuts import render, redirect
from .models import Alumni
from .forms import AlumniForm, YearFilterForm

def add_alumni(request):
    if request.method == 'POST':
        form = AlumniForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filter_alumni')
    else:
        form = AlumniForm()
    return render(request, 'add_alumni.html', {'form': form})

def filter_alumni(request):
    alumni = []
    if request.method == 'POST':
        form = YearFilterForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['passing_year']
            alumni = Alumni.objects.filter(passing_year=year)
    else:
        form = YearFilterForm()
    return render(request, 'filter_alumni.html', {'form': form, 'alumni': alumni})