from django import forms
from .models import Donacion
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
            "email",
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
                }
            ),
            "imagen": CustomClearableFileInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


# class JugadorBusquedaFormulario(forms.Form):
#     nombre = forms.CharField(required=False)
