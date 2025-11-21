from django import forms
from .models import OrderModels


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModels
        fields = '__all__'
