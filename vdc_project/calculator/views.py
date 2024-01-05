from django.shortcuts import render
from django.http import HttpResponse
from .models import ViaAdministracion
# Create your views here.

def index(request):
    return render(request, "calculator/index.html")

