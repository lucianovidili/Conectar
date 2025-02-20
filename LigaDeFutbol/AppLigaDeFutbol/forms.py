from django import forms
from .models import Jugador, Donacion
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms.widgets import ClearableFileInput


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = "Borrar"
    initial_text = "Imagen actual"
    input_text = "Cambiar"


class DonacionFormulario(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = [
            "titulo",
            "descripcion",
            "imagen",
            "propietario",
            "telefono",
            "contrasenia",
        ]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control"}),
            "propietario": forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.NumberInput(attrs={"class": "form-control"}),
            "contrasenia": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Se solicitará al intentar borrar o editar esta donación",
                }
            ),
            "imagen": CustomClearableFileInput(attrs={"class": "form-control"}),
        }


class JugadorFormulario(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = [
            "nombre",
            "apellido",
            "descripcion",
            "posicion",
            "promedio",
            "pierna_habil",
            "transferible",
            "imagen",
        ]
        # exclude = ['usuario']
        # widgets = {
        #     'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        #     'apellido' : forms.TextInput(attrs={'class': 'form-control'}),
        #     'posicion' : forms.Select(attrs={'class': 'form-control'}),
        #     'promedio' : forms.TextInput(attrs={'class': 'form-control'}),
        #     'pierna_habil' : forms.TextInput(attrs={'class': 'form-control'}),
        #     'transferible' : forms.Select(attrs={'class': 'form-control'}),
        # }


class JugadorBusquedaFormulario(forms.Form):
    nombre = forms.CharField(required=False)


# class OfertaFormulario(forms.ModelForm):
#     class Meta:
#         model = Oferta
#         fields = ["monto_ofrecido"]
