from django.conf.urls import url, include
from apps.crudjugadores.views import JugadorCreate, JugadorList, JugadorDelete, JugadorShow
from .views import *


def home(request):
    return render(request, 'base/base.html')

urlpatterns = [
    url(r'^$',home, name = "index"),
    url(r'^nuevo/',JugadorCreate.as_view(), name = "jugador_crear"),
    url(r'^listar/',JugadorList.as_view(), name = "jugador_listar"),
    url(r'^editar/(?P<pk>\d+)/$',JugadorUpdate.as_view(), name = "jugador_editar"),
    url(r'^eliminar/(?P<pk>\d+)/$',JugadorDelete.as_view(), name = "jugador_eliminar"),
    url(r'^show/(?P<pk>\d+)/$',JugadorShow.as_view(), name = "jugador_show"),
    # url(r'^buscar/$',search.as_view(), name = "jugador_buscar"),
]


"""
def home(request):
    return render(request, 'base.html')


urlpatterns = [
    url(r'^$',home, name = "index"),
    url(r'^crear_mascota/',CreateMascota.as_view(), name = "crear_mascota"),
    url(r'^listar_mascota/',ListMascota.as_view(), name = "listar_mascota"),
    url(r'^editar_mascota/(?P<pk>\d+)/$',UpdateMascota.as_view(), name = "editar_mascota"),
    url(r'^eliminar_mascota/(?P<pk>\d+)/$',DeleteMascota.as_view(), name = "eliminar_mascota"),    
]
"""
