from django.db import models
from apps.users.models import User

class ToDo(models.Model):
    user = models.ForeignKey(
        User, related_name="user_todo",
        verbose_name="Пользователь",
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
        unique=True
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Завершено"
    ) 
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата создания"
    )
    image = models.ImageField(
        upload_to='todo_images/',
        verbose_name='Фотография дела',
        blank=True, null=True
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Дело"
        verbose_name_plural = "Дела"