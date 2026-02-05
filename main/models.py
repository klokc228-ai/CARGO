from django.db import models

class Lead(models.Model):
    name = models.CharField("Имя", max_length=100)
    telegram = models.CharField("Telegram", max_length=100)
    cargo_type = models.CharField("Тип груза", max_length=200)
    additional_info = models.TextField("Доп. информация", blank=True, null=True)
    created_at = models.DateTimeField("Дата заявки", auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.telegram})"
