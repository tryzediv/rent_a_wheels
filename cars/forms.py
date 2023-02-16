from django import forms


class CarsFilterForm(forms.Form):
    query = forms.CharField(label='Поиск', required=False)
    min_price = forms.IntegerField(label='Цена от', required=False)
    max_price = forms.IntegerField(label='Цена до', required=False)
    min_year = forms.IntegerField(label='Год от', required=False)
    max_year = forms.IntegerField(label='Год до', required=False)
    selector = forms.ChoiceField(choices=(('', ''), ('АКПП', 'АКПП'), ('МКПП', 'МКПП')), label='КПП', required=False)
