from django.shortcuts import render
from cars.models import Car


def cars_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/cars_list.html', {'cars': cars})
