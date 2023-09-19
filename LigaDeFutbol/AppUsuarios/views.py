from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .forms import UsuarioRegistroFormulario, UserEditForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Avatar


class logueo(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')

    def get_success_url(self):
        return reverse_lazy('Inicio')
        
class registro(FormView):
    template_name = 'registro.html'
    form_class = UsuarioRegistroFormulario
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')

    def form_valid(self, form):
        form.instance.avatar = Avatar()
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(registro, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('Inicio')
        return super(registro, self).get(*args, **kwargs)

def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                usuario.avatar.save()
                
            miFormulario.save()
            return redirect('Inicio')
    else:
        avatar, created = Avatar.objects.get_or_create(user=request.user)
        miFormulario = UserEditForm(initial={'imagen': avatar.imagen}, instance=request.user)
        return render(request, 'perfil_editar.html', {'miFormulario': miFormulario, 'usuario': usuario.username})

# class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
#     template_name = 'cambiar_contrasenia.html'
#     success_url = reverse_lazy('EditarPerfil')

# class UsuarioEdicion(UpdateView):
#     form_class = FormularioEdicion
#     template_name= 'base/edicionPerfil.html'
#     success_url = reverse_lazy('home')

#     def get_object(self):
#         return self.request.user

# class CambioPassword(PasswordChangeView):
#     form_class = FormularioCambioPassword
#     template_name = 'base/passwordCambio.html'
#     success_url = reverse_lazy('password_exitoso')

# def password_exitoso(request):
#     return render(request, 'base/passwordExitoso.html', {})
