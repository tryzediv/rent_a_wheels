from django import forms
from orders.models import Order
from cars.models import Car


class OrderForm(forms.ModelForm):
    personal_data = forms.BooleanField(label='Я согласен на обработку персональных данных', required=True)
    car = forms.ModelChoiceField(queryset=Car.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Order
        fields = ['car', 'name', 'phone', 'email']
