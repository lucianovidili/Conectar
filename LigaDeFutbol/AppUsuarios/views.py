from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import UsuarioRegistroFormulario, UserEditForm
from django.contrib.auth import login
from .models import Avatar


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
