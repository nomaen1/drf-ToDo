from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(
        verbose_name="Ваша почта",
        unique=True
    )
    phone_number = models.CharField(
        verbose_name="Номер телефона",
        max_length=255
    )
    age = models.CharField(
        verbose_name="Возраст",
        max_length=255
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата создания"
    )

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'