import django_filters
from apps.crudjugadores.models import Jugador

class JugadorFilter(django_filters.FilterSet):
    class Meta:
        model = Jugador
        field = ['id','nombres','email',]