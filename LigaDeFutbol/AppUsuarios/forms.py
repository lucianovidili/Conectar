from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
    PasswordChangeForm,
)
from django import forms
from django.contrib.auth.models import User


class UsuarioRegistroFormulario(UserCreationForm):
    first_name = forms.CharField(
        max_length=20,
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        max_length=20,
        label="Apellido",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    username = forms.CharField(
        max_length=20,
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password1 = forms.CharField(
        label="Contraseña", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Repita Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class UserEditForm(UserChangeForm):
    contrasenia = None
    email = forms.EmailField(label="E-mail: ")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    imagen = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "imagen"]
