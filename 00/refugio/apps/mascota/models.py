from django.db import models
from apps.adopcion.models import Persona

# Create your models here.


class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Vacuna"
        verbose_name_plural = "Vacunas"

    # Para que muestre el nombre
    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()

    created = models.DateTimeField(auto_now_add=True, verbose_name ="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name ="Fecha de Edición")

    # Relacion Unos a Varios
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)

    # Relacion de Muchos es a Muchos
    vacuna = models.ManyToManyField(Vacuna, blank=True)

    class Meta:
        verbose_name = "mascota"
        verbose_name_plural = "Mascotas"
        ordering = ["-created"]

    # Para que muestre el nombre
    def __str__(self):
        return self.nombre
