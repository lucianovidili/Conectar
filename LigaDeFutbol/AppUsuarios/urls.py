from django.urls import path
from AppUsuarios import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.logueo.as_view(), name='Login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('registro/', views.registro.as_view(), name='Registro'),
    path('editarPerfil/', views.editar_perfil, name='EditarPerfil'),
]