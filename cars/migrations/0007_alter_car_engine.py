# Generated by Django 3.2.18 on 2023-02-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20230215_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.FloatField(default=1.4, max_length=50, verbose_name='Объем двигателя'),
        ),
    ]
