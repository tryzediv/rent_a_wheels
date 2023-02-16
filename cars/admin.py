from django.contrib import admin
from cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'engine', 'power', 'transmission', 'price', 'active']
    list_filter = ['active']
    search_fields = ['name', 'year', 'engine', 'power', 'transmission', 'price']
