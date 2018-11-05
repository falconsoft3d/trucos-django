from django.shortcuts import render
from apps.crudjugadores.models import Jugador
from apps.crudjugadores.forms import JugadorForm
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
# from apps.crudjugadores.filters import JugadorFilter

# Create your views here.

class JugadorCreate(CreateView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'crudjugadores/jugador_form.html'
    success_url = reverse_lazy('jugador_listar')


class JugadorList(ListView):
    queryset = Jugador.objects.order_by('id')
    template_name = 'crudjugadores/jugador_list.html'
    paginate_by = 5



class JugadorUpdate(UpdateView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'crudjugadores/jugador_form.html'
    success_url = reverse_lazy('jugador_listar')


class JugadorDelete(DeleteView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'crudjugadores/jugador_delete.html'
    success_url = reverse_lazy('jugador_listar')


class JugadorShow(DetailView):
    model = Jugador
    template_name = 'crudjugadores/jugador_show.html'


"""
def search(request):
    Jugador_list = Jugador.objects.all()
    Jugador_filter = JugadorFilter(request.GET, queryset=jugador_list)
    return render(request, 'crudjugadores/jugador_listar2.html', {'filter': jugador_filter})
"""

