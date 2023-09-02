from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .choices import transferible_opciones

# Create your models here.

class Club(models.Model):
    nombre = models.CharField(max_length=40)
    fundacion = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    posicion = models.CharField(max_length=40)
    promedio = models.IntegerField(default=80, validators=[MaxValueValidator(100, "Asegúrese de ingresar un valor menor o igual a 100"), MinValueValidator(0, "Asegúrese de ingresar un valor mayor o igual a 0")])
    pierna_habil = models.CharField(max_length=40)
    transferible = models.CharField(max_length=10, choices=transferible_opciones, default='no', verbose_name='Transferible')
    
    def __str__(self):
        return self.nombre + " " + self.apellido + ", " + self.posicion + ", " + str(self.promedio) + "prom, " + self.pierna_habil
    
class DirectorTecnico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    tactica_preferida = models.CharField(max_length=30)
    
    def __str__(self):
        return self.apellido
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
class Oferta(models.Model):
    usuario_nombre = models.CharField(max_length=60)
    jugador = models.ForeignKey(Jugador, related_name='jugadores', on_delete=models.CASCADE, null=True)
    monto_ofrecido = models.IntegerField(verbose_name='Monto ofrecido (U$D)')