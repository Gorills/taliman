from django.db import models
from djsingleton.models import SingletonModel
# Create your models here.

class Config(SingletonModel):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название компании')
    logo_img = models.ImageField(upload_to='setup', verbose_name='Логотип', null=True, blank=True)
    logo_text = models.CharField(max_length=100, verbose_name='Текстовый логотип', null=True, blank=True)
    time = models.CharField(max_length=150, verbose_name='Время работы')
    email = models.CharField(max_length=100, verbose_name='Почта')
    map = models.TextField(verbose_name='Код карты', null=True, blank=True)

    class Meta:
        verbose_name = 'Общая настройка сайта'
        verbose_name_plural = 'Общие настройки сайта'


class Social(models.Model):
    icon = models.CharField(max_length=250, verbose_name='Иконка (fontawesome.com)')
    link = models.CharField(max_length=100, verbose_name='Полная ссылка (с доменным именем)')
    parent = models.ForeignKey(Config, on_delete=models.CASCADE, related_name='social')

    class Meta:
        verbose_name = 'Социальные сети'
        verbose_name_plural = 'Социальные сети'


class Phone(models.Model):
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    name = models.CharField(max_length=150, verbose_name='Отображаемое название', null=True)
    parent = models.ForeignKey(Config, on_delete=models.CASCADE, related_name='phone')
    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'



class Meta(SingletonModel):
    meta_title = models.CharField(max_length=200, verbose_name='Мета заголовок')
    meta_description = models.CharField(max_length=350, verbose_name='Мета описание')
    meta_subtitle = models.CharField(max_length=150, verbose_name='Вторая часть заголовка сайта (через | )')
    meta_keywords = models.CharField(max_length=350, verbose_name='Ключевые слова')
    domen = models.CharField(max_length=350, verbose_name='Полный адрес сайта')

    class Meta:
        verbose_name = 'Мета настройка сайта'
        verbose_name_plural = 'Мета настройки сайта'


class Breadcrumbs(SingletonModel):
    about = models.ImageField(upload_to='breadcrumbs', verbose_name='О нас')
    service = models.ImageField(upload_to='breadcrumbs', verbose_name='Услуги')
    contact = models.ImageField(upload_to='breadcrumbs', verbose_name='Контакты')
    portfolio = models.ImageField(upload_to='breadcrumbs', verbose_name='Портфолио')
    rewiew = models.ImageField(upload_to='breadcrumbs', verbose_name='Отзывы')
    sale = models.ImageField(upload_to='breadcrumbs', verbose_name='Акции')

    class Meta:
        verbose_name = 'Изображение для хлебных крошек'
        verbose_name_plural = 'Изображения для хлебных крошек'
