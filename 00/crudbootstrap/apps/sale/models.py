from django.db import models

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key = True)
    rut = models.CharField(max_length = 12)
    razon_social = models.CharField(max_length = 255)
    direccion = models.CharField(max_length = 255)
    comuna = models.CharField(max_length = 255)
    giro = models.CharField(max_length = 255)

    def __str__(self):
        return self.razon_social
