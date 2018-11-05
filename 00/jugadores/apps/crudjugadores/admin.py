from django.contrib import admin

# Register your models here.

from apps.crudjugadores.models import Jugador,Deporte

# Register your models here.
admin.site.register(Jugador)
admin.site.register(Deporte)