from django.contrib import admin

from .models import Mascota, Vacuna

# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
  

admin.site.register(Mascota, MascotaAdmin)

admin.site.register(Vacuna)

