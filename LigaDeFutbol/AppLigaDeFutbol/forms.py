from django import forms
from .models import Jugador, DirectorTecnico, Club, Oferta
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class JugadorFormulario(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'apellido', 'posicion', 'promedio', 'pierna_habil', 'transferible', 'imagen']
        # exclude = ['usuario']
    
class DirectorTecnicoFormulario(forms.ModelForm):
    class Meta:
        model = DirectorTecnico
        fields = '__all__'
        
class ClubFormulario(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'
        
class JugadorBusquedaFormulario(forms.Form):
    nombre = forms.CharField(required=False)
    
class UserEditForm(UserChangeForm):
    contrasenia = None
    email = forms.EmailField(label="E-mail: ")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    imagen = forms.ImageField(label="Avatar", required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'imagen']
        
        
class OfertaFormulario(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['monto_ofrecido']