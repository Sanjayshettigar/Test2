from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_alumni, name='add_alumni'),
    path('filter/', views.filter_alumni, name='filter_alumni'),
]