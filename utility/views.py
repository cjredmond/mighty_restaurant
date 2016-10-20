from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
# Create your views here.

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'
