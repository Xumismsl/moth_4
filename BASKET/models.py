from django.db import models
from books.models import Book
from django.core.validators import RegexValidator


phone_validator = RegexValidator(
    regex=r'^\+996 \d{3} \d{3} \d{3}$',
    message="Номер должен быть в формате +996 XXX XXX XXX, где X — цифра"
)

class OrderModels(models.Model):
    PAYMENT = (
        ('Карта', 'Карта'),
        ('Наличные', 'Наличные'),
    )

    DELIVERY_CHOICES = (
        ('courier', 'Курьер'),
        ('pickup', 'Самовывоз'),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    payment_method = models.CharField(max_length=20, choices=PAYMENT, verbose_name='Способ оплаты')
    delivery_method = models.CharField(max_length=20, choices=DELIVERY_CHOICES, verbose_name='Способ доставки')
    address = models.CharField(max_length=100, verbose_name='Адрес доставки')
    telephone = models.CharField(max_length=16, validators=[phone_validator], verbose_name='Телефон')
