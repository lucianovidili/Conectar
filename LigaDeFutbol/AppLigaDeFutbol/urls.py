from django.urls import path
from AppLigaDeFutbol import views

# Para las imágenes
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('jugadorFormulario/', views.agregar_jugador, name="JugadorFormulario"),
    path('dtFormulario/', views.agregar_director_tecnico, name="DTFormulario"),
    path('clubFormulario/', views.agregar_club, name="ClubFormulario"),
    path('buscarPorNombre/', views.buscar_jugadores_por_nombre, name='BuscarJugadoresPorNombre'),
    path('jugadoresTransferibles/', views.listar_jugadores.as_view(), name='JugadoresTransferibles'),
    path('eliminarJugador/<int:pk>', views.eliminar_jugador.as_view(), name='EliminarJugador'),
    path('verJugador/<int:id>', views.ver_jugador, name='VerJugador'),
    path('comprarJugador/<int:id>', views.comprar_jugador, name='ComprarJugador'),
    path('editarJugador/<int:pk>', views.editar_jugador.as_view(), name='EditarJugador'),
    path('editarPerfil/', views.editar_perfil, name='EditarPerfil'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)