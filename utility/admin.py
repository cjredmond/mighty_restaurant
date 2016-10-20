from django.contrib import admin
from utility.models import Table, Order, Food, Profile

admin.site.register([Table, Order, Food, Profile])
