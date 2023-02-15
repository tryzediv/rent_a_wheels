from django.shortcuts import render, get_object_or_404
from cars.models import Car


def cars_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/cars_list.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})

