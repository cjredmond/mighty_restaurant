from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView
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
    def get_success_url(self):
        if self.request.user.profile.status == "o":
            success_url = reverse_lazy('profile_view')
        elif self.request.user.profile.status == "c":
            success_url = reverse('cook_view')
        return success_url


    def get_context_data(self):
        context = super().get_context_data()
        food = Food.objects.all()
        order = Order.objects.all()
        context['order'] = order
        context['food'] = food
        return context

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

class IndexView(TemplateView):
    template_name = "index.html"

class FoodCreateView(CreateView):
    model = Food
    success_url = reverse_lazy('food_list_view')
    fields = ('food', 'description', 'price')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super().form_valid(form)

class FoodListView(ListView):
    model = Food

    def get_context_data(self):
        context = super().get_context_data()
        context['object_list'] = Food.objects.all()
        return context

class ServerView(TemplateView):
    template_name = "server.html"

class OrderUpdateView(UpdateView):
    model = Order
    success_url = "/"
    fields = ("finished",)

class CookView(ListView):
    model = Order
