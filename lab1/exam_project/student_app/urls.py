from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student, name='add_student'),
    path('list/', views.student_list, name='student_list'),
    path('delete-unpaid/', views.delete_unpaid, name='delete_unpaid'),
]