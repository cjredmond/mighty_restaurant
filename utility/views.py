from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from utility.models import Profile, Food, Table, Order
# Create your views here.

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'

class ProfileUpdateView(UpdateView):
    template_name = "profile.html"
    fields = ('status', )
    success_url = reverse_lazy('profile_view')

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

class IndexView(TemplateView):
    template_name = "index.html"

class FoodCreateView(CreateView):
    model = Food
    success_url = '/'
    fields = ('food', 'description', 'price')
