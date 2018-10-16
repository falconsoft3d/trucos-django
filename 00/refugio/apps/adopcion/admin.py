from django.contrib import admin
from .models import Persona

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Persona, PersonaAdmin)
