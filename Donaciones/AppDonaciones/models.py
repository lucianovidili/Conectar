from django.db import models
from django.utils.timezone import now


class Donacion(models.Model):
    fecha_creacion = models.DateTimeField(default=now, blank=True, null=True)
    titulo = models.CharField(max_length=90, null=False, blank=False)
    # transferible = models.CharField(max_length=10, choices=transferible_opciones, default='no', verbose_name='Transferible')
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(
        upload_to="assets/img/donaciones",
        null=True,
        blank=True,
    )
    propietario = models.CharField(max_length=90, null=False, blank=False)
    telefono = models.IntegerField(blank=False, null=False)
    contrasenia = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Contraseña"
    )
    email = models.EmailField(max_length=254, verbose_name="E-mail", unique=False)
