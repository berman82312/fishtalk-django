from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

# Create your views here.
from .forms import UserCreationForm


class SignupPageView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
