from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Especie)
admin.site.register(ViaAdministracion)
admin.site.register(UnidadConcentracion)
admin.site.register(Medicamento)
admin.site.register(Paciente)