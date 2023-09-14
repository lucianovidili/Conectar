from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .forms import JugadorFormulario, DirectorTecnicoFormulario, ClubFormulario, OfertaFormulario, JugadorBusquedaFormulario
from .models import Jugador, Oferta
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# INICIO

class inicio(TemplateView):
    template_name = "inicio.html"

# JUGADOR

class crear_jugador(LoginRequiredMixin, CreateView):
    model = Jugador
    form_class = JugadorFormulario
    success_url = reverse_lazy('Inicio')
    template_name = 'jugador_formulario.html'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(crear_jugador, self).form_valid(form)

class editar_jugador(LoginRequiredMixin, UpdateView):
    model = Jugador
    template_name = 'jugador_formulario.html'
    fields = ['nombre', 'apellido', 'posicion', 'promedio', 'pierna_habil', 'transferible', 'imagen']
    success_url = reverse_lazy('JugadoresPlantilla')

class eliminar_jugador(LoginRequiredMixin, DeleteView):
    model = Jugador
    template_name = 'jugador_eliminar.html'
    success_url = reverse_lazy('JugadoresPlantilla')

class listar_jugadores_transferibles(LoginRequiredMixin, ListView):
    template_name = 'jugadores_transferibles.html'
    context_object_name = 'jugadores'
    model = Jugador
    
class listar_jugadores_plantilla(LoginRequiredMixin, ListView):
    template_name = 'jugadores_plantilla.html'
    context_object_name = 'jugadores'
    model = Jugador

@login_required
def ver_jugador(request, id, plantilla):
    jugador = Jugador.objects.get(pk=id)
    ofertas = Oferta.objects.filter(jugador__nombre=jugador.nombre)
    return render(request, 'jugador_ver.html', {'jugador': jugador, 'plantilla': plantilla, 'ofertas': ofertas})

@login_required    
def ofertar_jugador(request, id, ver_jugador):
    if request.method == 'POST':
        form = OfertaFormulario(request.POST)
        jugador = Jugador.objects.get(pk=request.POST.get("jugador_id"))
        usuario_nombre = request.POST.get("usuario_nombre")
        form.instance.jugador = jugador
        form.instance.usuario_nombre = usuario_nombre
        if form.is_valid():
            form.save()
            return redirect('Inicio')
    else:
        jugador = Jugador.objects.get(pk=id)
        form = OfertaFormulario()
        form.instance.jugador = jugador
    return render(request, 'jugador_ofertar.html', {'form': form, 'jugador': jugador, 'ver_jugador': ver_jugador})

# DIRECTOR TÉCNICO

def agregar_director_tecnico(request):
    if request.method == 'POST':
        form = DirectorTecnicoFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BuscarJugadoresPorNombre')
    else:
        form = DirectorTecnicoFormulario()
    return render(request, 'director_tecnico_formulario.html', {'form': form})

# CLUB

def agregar_club(request):
    if request.method == 'POST':
        form = ClubFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BuscarJugadoresPorNombre')
    else:
        form = ClubFormulario()
    return render(request, 'club_formulario.html', {'form': form})

# BUSCAR JUGADORES

def buscar_jugadores_por_nombre(request):
    jugadores = []
    form = JugadorBusquedaFormulario(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Jugador por nombre
        if nombre:
            jugadores = Jugador.objects.filter(nombre__icontains=nombre)

    return render(request, 'jugadores_buscar.html', {'form': form, 'jugadores': jugadores})
    