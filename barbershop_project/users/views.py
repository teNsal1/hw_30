from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserLoginForm

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('landing')  # Редирект на главную после регистрации

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)  # Автоматический вход после регистрации
        return response

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True  # Перенаправлять уже авторизованных пользователей

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('landing')  # Редирект на главную после выхода