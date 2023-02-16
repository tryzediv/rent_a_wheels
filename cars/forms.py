from django import forms


class CarsFilterForm(forms.Form):
    min_price = forms.IntegerField(label='Цена от', required=False)
    max_price = forms.IntegerField(label='Цена до', required=False)
    min_year = forms.IntegerField(label='Год от', required=False)
    max_year = forms.IntegerField(label='Год до', required=False)
    selector = forms.ChoiceField(label='КПП', required=False, choices=[
        ('', ''),
        ('АКПП', 'АКПП'),
        ('МКПП', 'МКПП')
    ])
    ordering = forms.ChoiceField(label='Сортировка', required=False, choices=[
        ('name', 'По названию'),
        ('price', 'Сначала недорогие'),
        ('-price', 'Сначала дорогие'),
        ('year', 'Сначала старые'),
        ('-year', 'Сначала новые')
    ])


class CarSearch(forms.Form):
    search = forms.CharField(label='Поиск', required=False)
