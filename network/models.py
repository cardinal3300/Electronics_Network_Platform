from django.core.exceptions import ValidationError
from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=200, verbose_name='Название')
    model = models.CharField(max_length=200, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.name} ({self.model})'


class RetailNetwork(models.Model):
    """Модель розничной сети электроники."""

    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )

    name = models.CharField(max_length=200, verbose_name='Название')

    level = models.IntegerField(choices=LEVEL_CHOICES)

    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    house_number = models.CharField(max_length=20, verbose_name='Номер дома')

    products = models.ManyToManyField(Product, verbose_name='Продукты')

    provider = models.ForeignKey('self',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='clients',
                                 verbose_name='Поставщик')

    debt = models.DecimalField(max_digits=20,
                               decimal_places=2,
                               default=0.00,
                               verbose_name='Задолженность перед поставщиком')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def clean(self):
        if self.provider == self:
            raise ValidationError('Объект не может ссылаться сам на себя')

    def __str__(self):
        return self.name
