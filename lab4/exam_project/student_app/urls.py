from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student, name='add_student'),
    path('amazon/', views.amazon_list, name='amazon_list'),
]