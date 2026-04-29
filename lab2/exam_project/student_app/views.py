from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('high_salary_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def high_salary_list(request):
    employees = Employee.objects.filter(salary__gt=50000)
    return render(request, 'list_employees.html', {'employees': employees})