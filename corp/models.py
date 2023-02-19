from django.core.exceptions import ValidationError
from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    title = models.CharField(
        verbose_name='Название товара',
        max_length=50,
        help_text='Введите название товара',
    )
    model = models.CharField(
        verbose_name='Модель товара',
        max_length=50,
        help_text='Введите модель',
    )
    release_date = models.DateField(
        verbose_name='Дата выхода на рынок',
        help_text='Укажите дату выхода на рынок товара',
    )

    def __str__(self):
        return self.title


class Contacts(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    email = models.EmailField(
        max_length=254,
        unique=True,
        help_text='Введите email предприятия',
    )
    country = models.CharField(
        verbose_name='Название страны',
        max_length=100,
        help_text='Страна предприятия',
    )
    city = models.CharField(
        verbose_name='Название города',
        max_length=100,
        help_text='Город предприятия',
    )
    street = models.CharField(
        verbose_name='Название улицы',
        max_length=100,
        help_text='Улица предприятия',
    )
    house_number = models.CharField(
        verbose_name='Номер дома',
        max_length=50,
        help_text='Номер дома предприятия',
    )

    def __str__(self):
        return self.email


class Company(models.Model):
    class Meta:
        verbose_name = 'Предприятие'
        verbose_name_plural = 'Предприятия'

    class Types(models.IntegerChoices):
        factory = 0, 'Завод'
        retail = 1, 'Розничная сеть'
        entrepreneur = 2, 'Индивидуальный предприниматель'

    hierarchy = models.SmallIntegerField(
        verbose_name='Тип компании',
        choices=Types.choices,
        help_text='Укажите тип компании',
    )
    title = models.CharField(
        verbose_name='Название компании',
        max_length=50,
        unique=True,
        help_text='Укажите название предприятия',
    )
    contacts = models.OneToOneField(
        'corp.Contacts',
        related_name='companies',
        on_delete=models.CASCADE,
        help_text='Укажите контактные дынные предприятия',
    )
    products = models.ManyToManyField(
        'corp.Product',
        related_name='companies',
        blank=True,
        help_text='Укажите продукты предприятия',
    )
    provider = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='Поставщик',
        related_name='traders',
        null=True,
        blank=True,
        help_text='Укажите поставщика',
    )
    debt = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name='Задолженность',
        default=0,
        help_text='Укажите задолженность предприятия',
    )
    pub_date = models.DateField(
        verbose_name='Время создания',
        auto_now_add=True,
    )

    def clean(self):
        if self.provider:
            if self.provider.id == self.id:
                raise ValidationError('Предприятие не может быть своим поставщиком')

    def __str__(self):
        return self.title
