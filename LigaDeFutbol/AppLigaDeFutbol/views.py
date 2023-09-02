from django.shortcuts import render, redirect
from AppLigaDeFutbol.forms import JugadorFormulario, DirectorTecnicoFormulario, ClubFormulario, OfertaFormulario, JugadorBusquedaFormulario, UserEditForm
from .models import Jugador
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


def inicio(request):
    return render(request, "inicio.html")

def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BuscarJugadoresPorNombre')
    else:
        form = JugadorFormulario()
    return render(request, 'jugador_formulario.html', {'form': form})

def ver_jugador(request, id):
    jugador = Jugador.objects.get(pk=id)
    return render(request, 'jugador_ver.html', {'jugador': jugador})

def comprar_jugador(request, id):
    if request.method == 'POST':
        form = OfertaFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Inicio')
    else:
        jugador = Jugador.objects.get(pk=id)
        form = OfertaFormulario()
    return render(request, 'jugador_comprar.html', {'form': form, 'jugador': jugador})

class listar_jugadores(ListView):
    template_name = 'jugadores_transferibles.html'
    context_object_name = 'jugadores'
    model = Jugador
    
class eliminar_jugador(DeleteView):
    model = Jugador
    template_name = 'jugador_eliminar.html'
    success_url = reverse_lazy('ListarJugadores')
    
class editar_jugador(UpdateView):
    model = Jugador
    # template_name = 'jugador_editar.html'
    template_name = 'jugador_formulario.html'
    fields = ['nombre', 'apellido', 'pierna_habil']
    success_url = reverse_lazy('ListarJugadores')

def agregar_director_tecnico(request):
    if request.method == 'POST':
        form = DirectorTecnicoFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BuscarJugadoresPorNombre')
    else:
        form = DirectorTecnicoFormulario()
    return render(request, 'director_tecnico_formulario.html', {'form': form})


def agregar_club(request):
    if request.method == 'POST':
        form = ClubFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BuscarJugadoresPorNombre')
    else:
        form = ClubFormulario()
    return render(request, 'club_formulario.html', {'form': form})


def buscar_jugadores_por_nombre(request):
    jugadores = []
    form = JugadorBusquedaFormulario(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Jugador por nombre
        if nombre:
            jugadores = Jugador.objects.filter(nombre__icontains=nombre)

    return render(request, 'jugadores_buscar.html', {'form': form, 'jugadores': jugadores})


def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                usuario.avatar.save()
                
            miFormulario.save()
            return redirect('Inicio')
    else:
        miFormulario = UserEditForm(initial={'imagen': usuario.avatar.imagen}, instance=request.user)
        return render(request, 'perfil_editar.html', {'miFormulario': miFormulario, 'usuario': usuario.username})

# class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
#     template_name = 'cambiar_contrasenia.html'
#     success_url = reverse_lazy('EditarPerfil')
    