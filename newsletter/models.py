from django.db import models


class Newsletter(models.Model):
    """Модель підпису на новини"""
    email = models.EmailField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Шанувальник'
        verbose_name_plural = 'Когорта шанувальників'

    def __str__(self):
        return self.email
