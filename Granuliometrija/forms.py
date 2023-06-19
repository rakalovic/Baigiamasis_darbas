from .models import Projektas, Duomenys
from django import forms

class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Projektas
        fields = '__all__'
        widgets = {
            'projekto_pavadinimas': forms.TextInput(attrs={
                'placeholder': 'Enter project name'
            }),
            'tyrimo_protokolo_numeris': forms.TextInput(attrs={
                'placeholder': 'Enter project name'
            }),
            'grezinio_nr': forms.TextInput(attrs={
                'placeholder' : 'Enter project name'
            }),
        }

