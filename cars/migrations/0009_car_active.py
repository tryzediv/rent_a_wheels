# Generated by Django 3.2.18 on 2023-02-16 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_auto_20230215_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
    ]
