from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name ="Titulo")
    description = models.TextField(verbose_name ="Descripción")
    image = models.ImageField(blank=True, upload_to='project', default='')
    link = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name ="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name ="Fecha de Edición")
    

    # Añadimos traduccion
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    # Para que muestre el nombre
    def __str__(self):
        return self.title