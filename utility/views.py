from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from utility.models import Profile, Food, Table, Order
from utility.forms import CookUpdateOrderForm
# Create your views here.

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'

class ProfileUpdateView(UpdateView):
    template_name = "profile.html"
    fields = ('status', )

    def get_success_url(self):
        # if self.request.user.profile.status == "o":
        success_url = reverse_lazy('profile_view')
        # elif self.request.user.profile.status == "c":
        #     success_url = reverse('cook_view')
        # else:
        #
        #     success_url = reverse_lazy('index_view')

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
    fields = ('food', 'description', 'price')

    def get_success_url(self, **kwargs):
        if self.request.user.profile.is_owner:
            success_url = reverse_lazy('food_list_view')
        else:
            target = Food.objects.last()
            number = target.order.id
            success_url = reverse_lazy('order_detail_view', args=[number,])
        return success_url

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super().form_valid(form)


class FoodListView(ListView):
    model = Food

    # def get_context_data(self):
    #     context = super().get_context_data()
    #     context['object_list'] = Food.objects.filter(owner='o')
        # admin = User.objects.get(username="admin")
        # context['object_list'] = Food.objects.filter(owner=admin)
        # all_food = Food.objects.filter(owner=admin)


        # return context

class ServerView(TemplateView):
    template_name = "server.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tables = Table.objects.all()
        context['tables'] = tables
        return context


class OrderUpdateView(UpdateView):
    model = Order
    def get_success_url(self):
        if self.request.user.profile.status == "c":
            success_url = reverse('cook_view')
        else:
            success_url = reverse('server_view')
        return success_url
    fields = ("finished", "paid")


class CookView(ListView):
    model = Order



class TableDetailView(DetailView):
    model = Table

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_list'] = Order.objects.filter(table=self.kwargs['pk'])
        return context

class OrderCreateView(CreateView):
    model = Order
    success_url = reverse_lazy('server_view')
    fields = ('food',)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.server = self.request.user
        target = Table.objects.get(id=self.kwargs['pk'])
        instance.table = target
        return super().form_valid(form)

class OrderDetailView(DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_list'] = Food.objects.filter(order = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        instance.form.save(commit=False)
        instance.server = self.request.user
        instance.order = self.kwargs['pk']
        return super().form_valid(form)
