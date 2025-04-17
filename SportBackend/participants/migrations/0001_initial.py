# Generated by Django 5.1.7 on 2025-04-13 05:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                
                ('phone_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='Номер телефона должен быть в формате +996XXXXXXXXX', regex='^\\+996[0-9]{9}$')])),
                ('city', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Город должен содержать только буквы, пробелы и дефис', regex='^[А-Яа-яЁё\\s-]+$')])),
                ('weight_category', models.IntegerField(validators=[django.core.validators.MinValueValidator(30, message='Весовая категория не может быть меньше 30 кг'), django.core.validators.MaxValueValidator(150, message='Весовая категория не может быть больше 150 кг')])),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(6, message='Возраст не может быть меньше 6 лет'), django.core.validators.MaxValueValidator(100, message='Возраст не может быть больше 100 лет')])),
                
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-registration_date'],
            },
        ),
    ]
