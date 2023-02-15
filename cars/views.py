from django.shortcuts import render, get_object_or_404
from cars.models import Car
from orders.forms import OrderForm


def cars_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/cars_list.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    form = OrderForm(request.POST or None, initial={'car': car})
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'cars/car_detail.html', {'car': car, 'form': form})

