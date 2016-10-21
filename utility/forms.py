from django import forms
from utility.models import Order

class CookUpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["finished",]
