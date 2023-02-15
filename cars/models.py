from django.db import models


class Car(models.Model):
    name = models.CharField('Название', max_length=50)
    year = models.IntegerField('Год выпуска')
    engine = models.FloatField('Объем двигателя', max_length=50, default=1.4)
    power = models.IntegerField('Мощность')
    body = models.CharField('Тип кузова', max_length=50)
    transmission = models.CharField('Тип коробки передач', max_length=50)
    price = models.IntegerField('Цена')
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['name']

    def __str__(self):
        return self.name
