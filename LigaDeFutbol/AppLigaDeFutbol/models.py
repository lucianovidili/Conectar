from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .choices import transferible_opciones, estado_oferta_opciones
from datetime import datetime


# class Club(models.Model):
#     nombre = models.CharField(max_length=40)
#     fundacion = models.IntegerField()

#     def __str__(self):
#         return self.nombre


class Donacion(models.Model):
    titulo = models.CharField(max_length=90, null=False, blank=False)
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


class Jugador(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    posicion = models.CharField(max_length=40)
    promedio = models.IntegerField(
        default=80,
        validators=[
            MaxValueValidator(
                100, "Asegúrese de ingresar un valor menor o igual a 100"
            ),
            MinValueValidator(0, "Asegúrese de ingresar un valor mayor o igual a 0"),
        ],
    )
    pierna_habil = models.CharField(max_length=40)
    transferible = models.CharField(
        max_length=10,
        choices=transferible_opciones,
        default="no",
        verbose_name="Transferible",
    )
    imagen = models.ImageField(upload_to="assets/img/jugadores", null=True, blank=True)

    def __str__(self):
        return (
            self.nombre
            + " "
            + self.apellido
            + ", "
            + self.posicion
            + ", "
            + str(self.promedio)
            + "prom, "
            + self.pierna_habil
        )


# class DirectorTecnico(models.Model):
#     nombre = models.CharField(max_length=30)
#     apellido = models.CharField(max_length=30)
#     tactica_preferida = models.CharField(max_length=30)

#     def __str__(self):
#         return self.apellido


# class Oferta(models.Model):
#     usuario_nombre = models.CharField(max_length=60)
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     jugador = models.ForeignKey(
#         Jugador, related_name="jugadores", on_delete=models.CASCADE, null=True
#     )
#     monto_ofrecido = models.IntegerField(verbose_name="Monto ofrecido (U$D)")
#     fecha_oferta = models.DateTimeField(default=datetime.now, blank=True)
#     estado = models.CharField(
#         max_length=13, choices=estado_oferta_opciones, default="no_contestada"
#     )

#     def __str__(self):
#         return f"{self.usuario_nombre} ofrece {self.monto_ofrecido}"
