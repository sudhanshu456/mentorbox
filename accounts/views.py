from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import PublicUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LogoutView,LoginView

# Create your views here.


class SignUpView(generic.CreateView):
    form_class = PublicUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class LoginView(LoginView):
    template_name='login.html'
    next_page='home'
    redirect_authenticated_user=True



class LogoutView(LogoutView):
    template_name='logout.html'
    next_page='home'
