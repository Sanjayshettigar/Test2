from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_faculty, name='add_faculty'),
    path('cse-profs/', views.cse_prof_list, name='cse_prof_list'),
]