from django.db import models


class Car(models.Model):
    name = models.CharField('Название', max_length=50)
    price = models.IntegerField('Цена')
    description = models.TextField('Описание', max_length=50)
    power = models.IntegerField('Мощность')
    body = models.CharField('Тип кузова', max_length=50)
