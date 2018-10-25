from django.conf import urls
from .views import *
from django.conf.urls import url, include

def home(request):
    return render(request, 'index.html')


urlpatterns = [
    url(r'^$',home, name = "index"),
    url(r'^crear_mascota/',CreateMascota.as_view(), name = "crear_mascota"),
    url(r'^listar_mascota/',ListMascota.as_view(), name = "listar_mascota"),
    url(r'^editar_mascota/(?P<pk>\d+)/$',UpdateMascota.as_view(), name = "editar_mascota"),
    url(r'^eliminar_mascota/(?P<pk>\d+)/$',DeleteMascota.as_view(), name = "eliminar_mascota"),    
]
