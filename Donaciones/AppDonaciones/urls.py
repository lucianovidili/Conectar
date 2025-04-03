from django.urls import path
from AppDonaciones import views

# Para las imágenes
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    DonacionListView,
    buscar_donaciones,
    exportar_excel,
    recuperar_contrasenia,
)

urlpatterns = [
    path("", views.inicio.as_view(), name="Inicio"),
    path(
        "crearEditarDonacion/",
        views.crear_donacion.as_view(),
        name="CrearEditarDonacion",
    ),
    # path(
    #     "buscarPorNombre/",
    #     views.buscar_jugadores_por_nombre,
    #     name="BuscarJugadoresPorNombre",
    # ),
    path(
        "listaDonaciones/",
        views.lista_donaciones,
        name="ListaDonaciones",
    ),
    path(
        "eliminarDonacion/<int:pk>",
        views.eliminar_donacion.as_view(),
        name="EliminarDonacion",
    ),
    path(
        "editarDonacion/<int:pk>",
        views.editar_donacion.as_view(),
        name="EditarDonacion",
    ),
    path(
        "api/listarDonaciones/",
        DonacionListView.as_view(),
        name="api_listar_donaciones",
    ),
    path(
        "listarDonaciones/", views.listar_donaciones, name="ListarDonaciones"
    ),  # URL para el frontend
    path(
        "api/listaDonaciones/", DonacionListView.as_view(), name="lista_donaciones_api"
    ),  # URL para la API
    path("buscar/", buscar_donaciones, name="buscar_donaciones"),
    path("exportar-excel/", exportar_excel, name="exportar_excel"),
    path(
        "recuperar-contrasenia/<int:id>",
        views.recuperar_contrasenia,
        name="RecuperarContrasenia",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
