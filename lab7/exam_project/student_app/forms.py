from django import forms
from .models import Alumni

class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = '__all__'

class YearFilterForm(forms.Form):
    passing_year = forms.IntegerField(label="Passing Year")