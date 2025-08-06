from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView as BaseLoginView
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserLoginForm

class RegisterView(CreateView):
    """Обработка регистрации новых пользователей"""
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('landing')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response

class UserLoginView(BaseLoginView):
    """Обработка аутентификации пользователей"""
    form_class = UserLoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'users/logout.html')
    
    def post(self, request):
        logout(request)
        return render(request, 'users/logout.html')