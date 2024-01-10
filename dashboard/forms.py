from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class HomeworkForm(forms.ModelForm):
    
    class Meta:
        model = Homework
        widgets = {'due':DateInput()}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']
