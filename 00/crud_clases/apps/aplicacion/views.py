from django.shortcuts import render,redirect

# Create your views here.

from .models import *
from .forms import MascotaForm
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse_lazy


"""
Formulario Basado en Clases
"""

def home(request):
    return render(request, 'index.html')

class CreateMascota(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'aplicacion/crear_mascota.html'
    success_url = reverse_lazy('index')

class ListMascota(ListView):
    model = Mascota
    template_name = 'aplicacion/listar_mascota.html'


class UpdateMascota(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'aplicacion/crear_mascota.html'
    success_url = reverse_lazy('index')


class DeleteMascota(DeleteView):
    model = Mascota
    template_name = 'aplicacion/eliminar_mascota.html'
    success_url = reverse_lazy('index')






