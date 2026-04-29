from django.db import models

class Faculty(models.Model):
    faculty_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
# Create your models here.
