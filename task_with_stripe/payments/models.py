from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=155, verbose_name='Название')
    description = models.TextField('Описание')
    price = models.IntegerField('Цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
