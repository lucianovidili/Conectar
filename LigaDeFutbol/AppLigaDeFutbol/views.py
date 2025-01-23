from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .forms import (
    JugadorFormulario,
    # DirectorTecnicoFormulario,
    # ClubFormulario,
    OfertaFormulario,
    JugadorBusquedaFormulario,
)
from .models import Jugador, Oferta
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse


# INICIO


class inicio(TemplateView):
    template_name = "inicio.html"


# JUGADOR


class crear_donacion(LoginRequiredMixin, CreateView):
    model = Jugador
    form_class = JugadorFormulario
    success_url = reverse_lazy("Inicio")
    template_name = "crear_editar_donacion.html"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(crear_donacion, self).form_valid(form)


class editar_jugador(LoginRequiredMixin, UpdateView):
    model = Jugador
    template_name = "jugador_formulario.html"
    fields = [
        "nombre",
        "apellido",
        "posicion",
        "promedio",
        "pierna_habil",
        "transferible",
        "imagen",
    ]
    success_url = reverse_lazy("JugadoresPlantilla")


class eliminar_jugador(LoginRequiredMixin, DeleteView):
    model = Jugador
    template_name = "jugador_eliminar.html"
    success_url = reverse_lazy("JugadoresPlantilla")


# class listar_jugadores_transferibles(LoginRequiredMixin, ListView):
def listar_donaciones(request):
    if (
        True
        # request.method == "GET"
        # and request.headers.get("X-Requested-With") == "XMLHttpRequest"
    ):
        page_number = request.GET.get("page", 1)
        jugadores = Jugador.objects.all().order_by("id")
        paginator = Paginator(jugadores, 5)  # 5 jugadores por página

        try:
            page = paginator.page(page_number)
        except:
            return JsonResponse({"jugadores": [], "has_more": False})

        jugadores_data = [
            {
                "id": jugador.pk,
                "nombre": jugador.nombre,
                "apellido": jugador.apellido,
                "imagen_url": jugador.imagen.url if jugador.imagen else None,
            }
            for jugador in page
        ]

        # return JsonResponse({"jugadores": jugadores_data, "has_more": page.has_next()})
        return render(request, "lista_donaciones.html", {"jugadores": jugadores})

    return render(request, "lista_donaciones.html", {"jugadores": jugadores})


@login_required
def listar_mis_donaciones(request, user, son_propias):
    # jugadores = Jugador.objects.all().order_by("id")
    # return render(request, "lista_mis_donaciones.html", {"jugadores": jugadores})
    jugadores = Jugador.objects.filter(usuario=user)
    return render(
        request,
        "lista_donaciones.html",
        {"jugadores": jugadores, "son_propias": son_propias},
    )


class listar_jugadores_plantilla(LoginRequiredMixin, ListView):
    template_name = "jugadores_plantilla.html"
    context_object_name = "jugadores"
    model = Jugador


def ver_jugador(request, id, plantilla):
    jugador = Jugador.objects.get(pk=id)
    ofertas = Oferta.objects.filter(jugador=jugador)
    return render(
        request,
        "jugador_ver.html",
        {"jugador": jugador, "plantilla": plantilla, "ofertas": ofertas},
    )


@login_required
def ofertar_jugador(request, id, ver_jugador):
    if request.method == "POST":
        form = OfertaFormulario(request.POST)
        jugador = Jugador.objects.get(pk=request.POST.get("jugador_id"))
        usuario_nombre = request.POST.get("usuario_nombre")
        form.instance.jugador = jugador
        form.instance.usuario_nombre = usuario_nombre
        form.instance.usuario = request.user
        if form.is_valid():
            form.save()
            return redirect("Inicio")
    else:
        jugador = Jugador.objects.get(pk=id)
        form = OfertaFormulario()
        form.instance.jugador = jugador
    return render(
        request,
        "jugador_ofertar.html",
        {"form": form, "jugador": jugador, "ver_jugador": ver_jugador},
    )


@login_required
def rechazar_oferta(request, id):
    oferta = Oferta.objects.get(pk=id)
    oferta.estado = "rechazada"
    oferta.save()
    return redirect("JugadoresPlantilla")


@login_required
def aceptar_oferta(request, id):
    oferta = Oferta.objects.get(pk=id)
    jugador = oferta.jugador
    jugador.usuario = oferta.usuario
    jugador.transferible = "no"
    jugador.save()
    ofertas = Oferta.objects.filter(jugador=jugador)
    ofertas.delete()
    return redirect("JugadoresPlantilla")


# DIRECTOR TÉCNICO


def agregar_director_tecnico(request):
    if request.method == "POST":
        form = DirectorTecnicoFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect("BuscarJugadoresPorNombre")
    else:
        form = DirectorTecnicoFormulario()
    return render(request, "director_tecnico_formulario.html", {"form": form})


# CLUB


def agregar_club(request):
    if request.method == "POST":
        form = ClubFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect("BuscarJugadoresPorNombre")
    else:
        form = ClubFormulario()
    return render(request, "club_formulario.html", {"form": form})


# BUSCAR JUGADORES


def buscar_jugadores_por_nombre(request):
    jugadores = []
    form = JugadorBusquedaFormulario(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get("nombre")

        # Realizar la búsqueda en el modelo Jugador por nombre
        if nombre:
            jugadores = Jugador.objects.filter(nombre__icontains=nombre)

    return render(
        request, "jugadores_buscar.html", {"form": form, "jugadores": jugadores}
    )
