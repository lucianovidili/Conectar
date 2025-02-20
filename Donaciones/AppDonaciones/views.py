from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .forms import (
    JugadorFormulario,
    # DirectorTecnicoFormulario,
    # ClubFormulario,
    DonacionFormulario,
    JugadorBusquedaFormulario,
)
from .models import Jugador, Donacion
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse


# INICIO


class inicio(TemplateView):
    template_name = "inicio.html"


# DONACIÓN


class crear_donacion(CreateView):
    model = Donacion
    form_class = DonacionFormulario
    success_url = reverse_lazy("ListaDonaciones")
    template_name = "crear_editar_donacion.html"

    # def form_valid(self, form):
    #     form.instance.propietario = self.request.user
    #     return super(crear_donacion, self).form_valid(form)


class editar_donacion(UpdateView):
    model = Donacion
    form_class = DonacionFormulario
    # fields = ["titulo", "descripcion", "imagen", "propietario", "telefono"]
    success_url = reverse_lazy("ListaDonaciones")
    template_name = "crear_editar_donacion.html"


class eliminar_donacion(DeleteView):
    model = Donacion
    template_name = "eliminar_donacion.html"
    success_url = reverse_lazy("ListaDonaciones")


# class listar_jugadores_transferibles(LoginRequiredMixin, ListView):
def listar_donaciones(request):
    if (
        False
        # request.method == "GET"
        # and request.headers.get("X-Requested-With") == "XMLHttpRequest"
    ):
        page_number = request.GET.get("page", 1)
        donaciones = Donacion.objects.all().order_by("id")
        paginator = Paginator(donaciones, 5)  # 5 jugadores por página

        try:
            page = paginator.page(page_number)
        except:
            return JsonResponse({"donaciones": [], "has_more": False})

        donaciones_data = [
            {
                "id": jugador.pk,
                "nombre": jugador.nombre,
                "apellido": jugador.apellido,
                "imagen_url": jugador.imagen.url if jugador.imagen else None,
            }
            for jugador in page
        ]

        # return JsonResponse({"jugadores": donaciones_data, "has_more": page.has_next()})
        return render(request, "lista_donaciones.html", {"donaciones": donaciones})

    donaciones = Donacion.objects.all().order_by("id")
    return render(request, "lista_donaciones.html", {"donaciones": donaciones})


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


# @login_required
# def ofertar_jugador(request, id, ver_jugador):
#     if request.method == "POST":
#         form = OfertaFormulario(request.POST)
#         jugador = Jugador.objects.get(pk=request.POST.get("jugador_id"))
#         usuario_nombre = request.POST.get("usuario_nombre")
#         form.instance.jugador = jugador
#         form.instance.usuario_nombre = usuario_nombre
#         form.instance.usuario = request.user
#         if form.is_valid():
#             form.save()
#             return redirect("Inicio")
#     else:
#         jugador = Jugador.objects.get(pk=id)
#         form = OfertaFormulario()
#         form.instance.jugador = jugador
#     return render(
#         request,
#         "jugador_ofertar.html",
#         {"form": form, "jugador": jugador, "ver_jugador": ver_jugador},
#     )


# @login_required
# def rechazar_oferta(request, id):
#     oferta = Oferta.objects.get(pk=id)
#     oferta.estado = "rechazada"
#     oferta.save()
#     return redirect("JugadoresPlantilla")


# @login_required
# def aceptar_oferta(request, id):
#     oferta = Oferta.objects.get(pk=id)
#     jugador = oferta.jugador
#     jugador.usuario = oferta.usuario
#     jugador.transferible = "no"
#     jugador.save()
#     ofertas = Oferta.objects.filter(jugador=jugador)
#     ofertas.delete()
#     return redirect("JugadoresPlantilla")


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
