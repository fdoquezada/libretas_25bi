from django import forms
from .models import EntregaLibreta, Conductor, Supervisor

class EntregaLibretaForm(forms.ModelForm):
    class Meta:
        model = EntregaLibreta
        fields = ['conductor', 'fecha_entrega', 'mes', 'anio', 'semana', 'estado']
        widgets = {
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}),
        }

class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = ['nombre', 'supervisor']

class SupervisorForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = ['nombre']