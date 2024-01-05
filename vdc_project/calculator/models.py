from django.db import models

# Create your models here.

# creo tabla para especies
class Especie(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    

# tabla para vias de administracion
class ViaAdministracion(models.Model):
    nombre = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.nombre
    

# tabla para unidad de concentracion  μg/ml , mg/ml, %
class UnidadConcentracion(models.Model):
    nombre = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.nombre
    

class UnidadDosis(models.Model):
    nombre = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.nombre

# tabla para medicamentos
class Medicamento(models.Model):
    nombre = models.CharField(max_length=60)
    dosis_maxima = models.FloatField()
    dosis_minima = models.FloatField()
    unidad_dosis = models.ForeignKey(UnidadDosis, on_delete=models.CASCADE, null=True)
    concentracion = models.FloatField()
    unidad_concentracion = models.ForeignKey(UnidadConcentracion, on_delete=models.CASCADE, related_name="drogas")
    vias_administracion = models.ManyToManyField(ViaAdministracion)
    especies = models.ManyToManyField(Especie)
    contraindicaciones=models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.nombre}, {self.concentracion} {self.unidad_concentracion}'


# tabla para paciente
class Paciente(models.Model):
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    peso = models.FloatField()

    def __str__(self):
        return f'{self.especie}, {self.peso} kg'
    