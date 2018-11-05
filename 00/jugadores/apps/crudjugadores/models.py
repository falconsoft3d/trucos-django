from django.db import models

# Create your models here.

class Deporte(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    email = models.CharField(max_length=50)
    deporte = models.ForeignKey(Deporte, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombres