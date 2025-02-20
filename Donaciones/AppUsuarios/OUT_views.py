from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .forms import UsuarioRegistroFormulario, UserEditForm, UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Avatar
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.profile.save()


class logueo(LoginView):
    template_name = "login.html"
    fields = "__all__"
    redirect_autheticated_user = True
    success_url = reverse_lazy("Inicio")

    def get_success_url(self):
        return reverse_lazy("Inicio")


class registro(FormView):
    template_name = "registro.html"
    form_class = UsuarioRegistroFormulario
    redirect_autheticated_user = True
    success_url = reverse_lazy("Inicio")

    def form_valid(self, form):
        form.instance.avatar = Avatar()
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(registro, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("Inicio")
        return super(registro, self).get(*args, **kwargs)


def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get("imagen"):
                usuario.avatar.imagen = miFormulario.cleaned_data.get("imagen")
                usuario.avatar.save()

            miFormulario.save()
            return redirect("Inicio")
    else:
        avatar, created = Avatar.objects.get_or_create(user=request.user)
        miFormulario = UserEditForm(
            initial={"imagen": avatar.imagen}, instance=request.user
        )
        return render(
            request,
            "perfil_editar.html",
            {"miFormulario": miFormulario, "usuario": usuario.username},
        )
