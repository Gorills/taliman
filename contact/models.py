from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    tel = models.CharField(max_length=20, verbose_name='Телефон')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    verbose_name = 'Обратный звонок'
    verbose_name_plural = 'Обратный звонок'

class Review(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    tel = models.CharField(max_length=20, verbose_name='Телефон')
    message = models.TextField(verbose_name='Текст отзыва')
    date = models.DateTimeField(auto_now_add=True)
    moderate = models.BooleanField(default=False, verbose_name='Опубликован')

    def __str__(self):
        return self.name

    verbose_name = 'Отзыв'
    verbose_name_plural = 'Отзывы'