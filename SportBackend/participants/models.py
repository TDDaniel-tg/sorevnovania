from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

class Participant(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[]  # Removed restrictive regex validator
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^(\+996[0-9]{9}|none)$',
                message='Номер телефона должен быть в формате +996XXXXXXXXX или "none"'
            )
        ]
    )
    city = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[А-Яа-яЁё\s-]+$',
                message='Город должен содержать только буквы, пробелы и дефис'
            )
        ]
    )
    weight_category = models.IntegerField(
        validators=[
            MinValueValidator(30, message='Весовая категория не может быть меньше 30 кг'),
            MaxValueValidator(150, message='Весовая категория не может быть больше 150 кг')
        ]
    )
    age = models.IntegerField(
        validators=[
            MinValueValidator(6, message='Возраст не может быть меньше 6 лет'),
            MaxValueValidator(100, message='Возраст не может быть больше 100 лет')
        ]
    )
    discipline = models.CharField(
        max_length=50,
        validators=[]  # Removed restrictive regex validator
    )
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        phone_display = self.phone_number if self.phone_number != "none" else "none"
        return f"{self.name} - {self.discipline} - {phone_display}"

    class Meta:
        ordering = ['-registration_date']