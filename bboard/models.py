from django.db import models


# Create your models here.
class Bb(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название'
    )
    body = models.TextField(
        max_length=500,
        verbose_name='Описание объявления',
        blank=True,
        null=True
    )
    price = models.FloatField(
        verbose_name='Цена',
        blank=True,
        null=True
    )
    rubric = models.ForeignKey(
        'Rubric',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Rubric(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
