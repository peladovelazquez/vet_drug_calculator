from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import ResultForm

# Create your views here.

def layout(request):

    medicamento = None
    volumen_final_minimo = None
    volumen_final_maximo = None

    #si el metodo es POST, crea un formulario con los datos enviados y asigna valor a medicamento
    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            peso = form.cleaned_data['peso']
            medicamento = form.cleaned_data['medicamento']
            unidadConcentracion = medicamento.unidad_concentracion
            volumen_final_minimo, volumen_final_maximo = calcular_volumen_final(medicamento.dosis_maxima, medicamento.dosis_minima, medicamento.concentracion, peso, UnidadConcentracion)
    # si el metodo es GET, muestra un formulario vacio, y al no haber medicamento, no se muestra en el template layout.html
    else:
        form = ResultForm()


    return render(request, 'calculator/layout.html', {
        "form" : form,
        "medicamento":medicamento,
        "volumenMinimo" : volumen_final_minimo,
        "volumenMaximo" : volumen_final_maximo

    })


#funcion para calcular dosis finales
def calcular_volumen_final(dosis_maxima, dosis_minima, concentracion, peso_paciente, unidad_concentracion):

    if unidad_concentracion == 'mg/ml':
        concentracion *= 1
    elif unidad_concentracion == '%':
        concentracion *= 0.01
    elif unidad_concentracion == 'μg/ml':
        concentracion *= 0.001


    dosis_minima_ajustada = min(dosis_minima, dosis_maxima)
    dosis_maxima_ajustada = min(dosis_maxima, dosis_maxima)

    volumen_final_minima = (dosis_minima_ajustada * peso_paciente) / concentracion
    volumen_final_maxima = (dosis_maxima_ajustada * peso_paciente) / concentracion

    return volumen_final_minima, volumen_final_maxima
