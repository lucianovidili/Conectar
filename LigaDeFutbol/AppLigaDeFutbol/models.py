from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

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
    
    def __str__(self):
        return self.apellido
    
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