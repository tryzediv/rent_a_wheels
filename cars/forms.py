from django import forms


class CarsFilterForm(forms.Form):
    min_price = forms.IntegerField(label='От', required=False)
    max_price = forms.IntegerField(label='До', required=False)
