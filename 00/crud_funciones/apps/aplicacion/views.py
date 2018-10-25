from django.shortcuts import render,redirect

# Create your views here.

from .models import *
from .forms import MascotaForm


"""
Formulario Basado en Funciones
"""



def crearMascota(request):
    if request.method == 'POST': 
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MascotaForm()
    return render(request,'aplicacion/crear_mascota.html',{'form':form})

def listarMascota(request):
    mascota = Mascota.objects.all()
    context = {'mascota':mascota}
    return render(request, 'aplicacion/listar_mascota.html',context)


def editarMascota(request, id):
    mascota = Mascota.objects.get(id = id)
    if request.method == 'GET':
        form = MascotaForm(instance = mascota)
    else:
        form = MascotaForm(request.POST, instance = mascota)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, 'aplicacion/crear_mascota.html',{'form':form})


def eliminarMascota(request, id):
    mascota = Mascota.objects.get(id = id)
    if request.method == 'POST':
        mascota.delete()
        return redirect('index')
    return render(request, 'aplicacion/eliminar_mascota.html', {'mascota':mascota})


