from django.db import models
from cars.models import Car
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    car = models.ForeignKey(Car, verbose_name='Автомобиль', on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=50)
    phone = PhoneNumberField(verbose_name='Телефон', unique=True, null=False, blank=False)
    date = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
