from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
    PasswordChangeForm,
)
from django import forms
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(
        max_length=15, blank=True, null=True
    )  # Campo para el teléfono

    def __str__(self):
        return self.user.username


class UsuarioRegistroFormulario(UserCreationForm):
    phone = forms.CharField(
        max_length=15,
        label="Teléfono",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super().save(commit=commit)
        phone = self.cleaned_data.get("phone")
        if commit:
            user.profile.phone = phone
            user.profile.save()
        return user


class UserEditForm(UserChangeForm):
    phone = forms.CharField(
        max_length=15,
        label="Teléfono",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False,
    )

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "phone"]

    def save(self, commit=True):
        user = super().save(commit=commit)
        phone = self.cleaned_data.get("phone")
        if commit:
            user.profile.phone = phone
            user.profile.save()
        return user
