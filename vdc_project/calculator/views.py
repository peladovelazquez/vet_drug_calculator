from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def layout(request):
    return render(request, "calculator/layout.html", {
        "medicamento" : Medicamento.objects.first()
    })

