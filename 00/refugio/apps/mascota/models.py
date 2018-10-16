from django.db import models

# Create your models here.


class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()

    created = models.DateTimeField(auto_now_add=True, verbose_name ="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name ="Fecha de Edición")
