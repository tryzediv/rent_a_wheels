from django.db import models
from cars.models import Car
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


class Order(models.Model):
    car = models.ForeignKey(Car, verbose_name='Автомобиль', on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=50)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(verbose_name='Телефон', validators=[phoneNumberRegex], max_length=16)
    date = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'