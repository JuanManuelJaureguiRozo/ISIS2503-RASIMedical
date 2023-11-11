from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'id',
            'tipocita',
            'dateTime',
        ]

        labels = {
            'nombre' : 'Nombre',
            'id' : 'ID',
            'tipocita' : 'Tipo Cita',
            'dateTime' : 'Date Time',
        }
