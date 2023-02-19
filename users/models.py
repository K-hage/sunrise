from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email адрес',
        max_length=254,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=50,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
    )

    company = models.ForeignKey(
        'corp.Company',
        on_delete=models.CASCADE,
        related_name='employees',
        null=True
    )

    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name',
        'password',
    ]

    def __str__(self):
        return self.username
