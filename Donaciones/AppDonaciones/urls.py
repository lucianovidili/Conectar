from django.urls import path
from AppDonaciones import views

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
    # path(
    #     "listaMisDonaciones/<str:user>/<int:son_propias>",
    #     views.listar_mis_donaciones,
    #     name="ListaMisDonaciones",
    # ),
    path(
        "jugadoresPlantilla/",
        views.listar_jugadores_plantilla.as_view(),
        name="JugadoresPlantilla",
    ),
    path(
        "eliminarDonacion/<int:pk>",
        views.eliminar_donacion.as_view(),
        name="EliminarDonacion",
    ),
    path("verJugador/<int:id>/<int:plantilla>", views.ver_jugador, name="VerJugador"),
    # path(
    #     "ofertarJugador/<int:id>/<int:ver_jugador>",
    #     views.ofertar_jugador,
    #     name="OfertarJugador",
    # ),
    # path("aceptarOferta/<int:id>", views.aceptar_oferta, name="AceptarOferta"),
    # path("rechazarOferta/<int:id>", views.rechazar_oferta, name="RechazarOferta"),
    path(
        "editarDonacion/<int:pk>",
        views.editar_donacion.as_view(),
        name="EditarDonacion",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
