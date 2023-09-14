from django import forms
from .models import Jugador, DirectorTecnico, Club, Oferta
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class JugadorFormulario(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'apellido', 'posicion', 'promedio', 'pierna_habil', 'transferible', 'imagen']
        # exclude = ['usuario']
        # widgets = {
        #     'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        #     'apellido' : forms.TextInput(attrs={'class': 'form-control'}),
        #     'posicion' : forms.Select(attrs={'class': 'form-control'}),
        #     'promedio' : forms.TextInput(attrs={'class': 'form-control'}),
        #     'pierna_habil' : forms.TextInput(attrs={'class': 'form-control'}),
        #     'transferible' : forms.Select(attrs={'class': 'form-control'}),                 
        # }
    
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
    
class OfertaFormulario(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['monto_ofrecido']