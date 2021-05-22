from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    tel = models.CharField(max_length=20, verbose_name='Телефон')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратный звонок'


class ContactPopup(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    tel = models.CharField(max_length=20, verbose_name='Телефон')
    
    message = models.TextField(verbose_name='Сообщение', null=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Контакты попап'
        verbose_name_plural = 'Контакты попап'


class ContactFull(models.Model):
    name_2 = models.CharField(max_length=100, verbose_name='Имя')
    tel_2 = models.CharField(max_length=20, verbose_name='Телефон')
    email_2 = models.EmailField(max_length=150, verbose_name='Email')
    theme_2 = models.CharField(max_length=100, verbose_name='Тема сообщения')
    message_2 = models.TextField(verbose_name='Сообщение', null=True)

    date_2 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_2
    class Meta:
        verbose_name = 'Заявки со страницы контктов'
        verbose_name_plural = 'Заявки со страницы контктов'




class Review(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    tel = models.CharField(max_length=20, verbose_name='Телефон')
    message = models.TextField(verbose_name='Текст отзыва')
    date = models.DateTimeField(auto_now_add=True)
    moderate = models.BooleanField(default=False, verbose_name='Опубликован')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'