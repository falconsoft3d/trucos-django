from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()

    created = models.DateTimeField(auto_now_add=True, verbose_name ="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name ="Fecha de Edición")

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ["-created"]

    # Para que muestre el nombre
    def __str__(self):
        return self.nombre