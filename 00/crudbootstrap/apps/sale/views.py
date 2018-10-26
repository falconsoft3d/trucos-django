from django.shortcuts import render,redirect

# Create your views here.

from .models import *
from .forms import ClienteForm
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, 'home.html')

class ListCliente(ListView):
    model = Cliente
    template_name = 'list.html'


class CreateCliete(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'crear_cliente.html'
    success_url = reverse_lazy('index')