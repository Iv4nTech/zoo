from .models import Animal, Veterinario, VacunaAnimal, Consulta
from django.forms import ModelForm
from django import forms
import datetime
from django.core.exceptions import ValidationError

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'sexo', 'fecha_nac', 'recinto', 'especie', 'foto']

        widgets = {
            'fecha_nac': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

    def clean_fecha_nac(self):
        fecha_nac = self.cleaned_data['fecha_nac']
        if fecha_nac > datetime.date.today():
            raise ValidationError('La fecha de nacimiento no puede ser mayor a la fecha actual')
        return fecha_nac

class VeterinarioForm(ModelForm):
    class Meta:
        model = Veterinario
        fields = ['nombre', 'especialidad', 'licencia', 'sexo', 'fecha_nac', 'telefono', 'foto']

        widgets = {
            'fecha_nac': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }


class VacunaAnimalForm(ModelForm):
    class Meta:
        model = VacunaAnimal
        fields = ['vacuna', 'lote', 'fecha_proxima_dosis', 'veterinario']

        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_proxima_dosis': forms.DateInput(attrs={'type': 'date'}),
        }


class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['diagnostico', 'tratamiento', 'fecha_hora', 'animal']

        widgets = {
            'fecha_hora': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'type': 'datetime-local'}),
        }