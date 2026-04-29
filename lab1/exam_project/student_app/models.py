from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20, unique=True)
    semester = models.CharField(max_length=10)
    fee_paid = models.BooleanField(default=False)  # Checked = Paid, Unchecked = Not Paid

    
