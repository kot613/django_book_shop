from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm, LoginUserForm


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    next_page = 'home'

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        print(form.errors)
        print(type(form.errors))
        print(type(form.errors['__all__']))
        return self.render_to_response(self.get_context_data(form=form))


def logout_user(request):
    logout(request)
    return redirect('home')
