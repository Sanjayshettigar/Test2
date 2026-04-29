from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_employee, name='add_employee'),
    path('list/', views.high_salary_list, name='high_salary_list'),
]