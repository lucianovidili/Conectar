from django.urls import path
from AppLigaDeFutbol import views

# Para las imágenes
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.inicio.as_view(), name="Inicio"),
    path(
        "crearEditarDonacion/",
        views.crear_donacion.as_view(),
        name="CrearEditarDonacion",
    ),
    path("dtFormulario/", views.agregar_director_tecnico, name="DTFormulario"),
    path("clubFormulario/", views.agregar_club, name="ClubFormulario"),
    path(
        "buscarPorNombre/",
        views.buscar_jugadores_por_nombre,
        name="BuscarJugadoresPorNombre",
    ),
    path(
        "listaDonaciones/",
        views.listar_donaciones,
        name="ListaDonaciones",
    ),
    path(
        "listaMisDonaciones/<str:user>/<int:son_propias>",
        views.listar_mis_donaciones,
        name="ListaMisDonaciones",
    ),
    path(
        "jugadoresPlantilla/",
        views.listar_jugadores_plantilla.as_view(),
        name="JugadoresPlantilla",
    ),
    path(
        "eliminarJugador/<int:pk>",
        views.eliminar_jugador.as_view(),
        name="EliminarJugador",
    ),
    path("verJugador/<int:id>/<int:plantilla>", views.ver_jugador, name="VerJugador"),
    path(
        "ofertarJugador/<int:id>/<int:ver_jugador>",
        views.ofertar_jugador,
        name="OfertarJugador",
    ),
    path("aceptarOferta/<int:id>", views.aceptar_oferta, name="AceptarOferta"),
    path("rechazarOferta/<int:id>", views.rechazar_oferta, name="RechazarOferta"),
    path(
        "editarJugador/<int:pk>", views.editar_jugador.as_view(), name="EditarJugador"
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
