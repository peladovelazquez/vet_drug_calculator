from django import forms
from .models import *

class ResultForm(forms.Form):
    especie = forms.ModelChoiceField(queryset=Especie.objects.all(), empty_label="Selecciona la especie")
    peso = forms.FloatField (label="Peso", widget=forms.TextInput)
    medicamento = forms.ModelChoiceField(queryset=Medicamento.objects.all(), to_field_name='nombre', empty_label="Selecciona el medicamento")
