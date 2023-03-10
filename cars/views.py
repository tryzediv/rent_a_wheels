from django.shortcuts import render, get_object_or_404
from cars.models import Car
from orders.forms import OrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from cars.forms import CarsFilterForm, CarSearch
from django.db.models import Q


def cars_list(request):
    cars = Car.objects.filter(active=True)
    form = CarsFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['min_price']:
            cars = cars.filter(price__gte=form.cleaned_data['min_price'])
        if form.cleaned_data['max_price']:
            cars = cars.filter(price__lte=form.cleaned_data['max_price'])
        if form.cleaned_data['min_year']:
            cars = cars.filter(year__gte=form.cleaned_data['min_year'])
        if form.cleaned_data['max_year']:
            cars = cars.filter(year__lte=form.cleaned_data['max_year'])
        if form.cleaned_data['selector']:
            cars = cars.filter(transmission__exact=form.cleaned_data['selector'])
        if form.cleaned_data['ordering']:
            cars = cars.order_by(form.cleaned_data['ordering'])
    return render(request, 'cars/cars_list.html', {'cars': cars, 'form': form})


def cars_search(request):
    cars = Car.objects.filter(active=True)
    search = CarSearch(request.GET)
    if search.cleaned_data['search']:
        cars = cars.filter(
            Q(body__icontains=search.cleaned_data['search']) |
            Q(name__icontains=search.cleaned_data['search']) |
            Q(year__icontains=search.cleaned_data['search']) |
            Q(engine__icontains=search.cleaned_data['search']) |
            Q(power__icontains=search.cleaned_data['search'])
        )
    return render(request, 'cars/cars_list.html', {'cars': cars, 'search': cars_search})


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    form = OrderForm(request.POST or None, initial={'car': car})

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            url = reverse('car', kwargs={'car_id': car.id})
            return HttpResponseRedirect(f'{url}?sent=1')

    return render(request, 'cars/car_detail.html', {
        'car': car,
        'form': form,
        'sent': request.GET.get('sent')
    })

