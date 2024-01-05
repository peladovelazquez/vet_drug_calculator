from django.contrib import admin

# Register your models here.
class MedicamentoAdmin(admin.ModelAdmin):
    filter_horizontal = ("vias_administracion", "especies")

from .models import *

admin.site.register(Especie)
admin.site.register(ViaAdministracion)
admin.site.register(UnidadConcentracion)
admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Paciente)
admin.site.register(UnidadDosis)