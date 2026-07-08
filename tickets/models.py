from django.db import models

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('done', 'Выполнена'),
    ]

    title = models.CharField("Тема", max_length=200)
    description = models.TextField("Описание")
    status = models.CharField(
        "Статус",
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    category = models.CharField("Категория (ИИ)", max_length=50, blank=True, null=True)
    draft_response = models.TextField("Черновик ответа (ИИ)", blank=True, null=True)


    def __str__(self):
        return f"{self.id}: {self.title}"

