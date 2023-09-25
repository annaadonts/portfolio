from django import forms
from .models import Programmer, Project

class ProgrammerForm(forms.ModelForm):
    class Meta:
        model = Programmer
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
