
from django.db import models
from django.urls import reverse
from django.utils.translation import activate

# Create your models here.
class Serv(models.Model):
    title = models.CharField(max_length=150, verbose_name='Назавние услуги')
    h1 = models.CharField(max_length=200, verbose_name='Заголовок H1', null=True)
    breadcrumbs = models.ImageField(upload_to='serv', null=True, blank=True)
    image_prew = models.ImageField(upload_to='serv', verbose_name='Основное изображение')
    description = models.CharField(max_length=300, verbose_name='Короткое описание')
    text = models.TextField(verbose_name='Описание')
    meta_title = models.CharField(max_length=100, verbose_name='Мета заголовок')
    meta_description = models.CharField(max_length=280, verbose_name='Мета описание')
    meta_keywords = models.CharField(max_length=200, verbose_name='Ключевые слова')
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('serv_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class ServBlock(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заголовок', null=True, blank=True)
    text = models.TextField(verbose_name='Текст блока')
    color = models.CharField(max_length=20, verbose_name='Цвет фона')
    text_color = models.CharField(max_length=20, verbose_name='Цвет текста', null=True, blank=True)
    bg = models.ImageField(upload_to='remontblock', verbose_name='Фон', null=True, blank=True)
    parent = models.ForeignKey(Serv, on_delete=models.CASCADE, related_name='block', verbose_name='цвет')
    button = models.CharField(max_length=150, verbose_name='Текст кнопки', null=True, blank=True)
    class Meta:
        verbose_name = 'Дополнительный блок'
        verbose_name_plural = 'Дополнительные блоки'

class ServImage(models.Model):
    name = models.CharField(max_length=250, verbose_name='Описание картинки')
    image = models.ImageField(upload_to='servimage', verbose_name='Изображение')
    parent = models.ForeignKey(Serv, on_delete=models.CASCADE, related_name='image', verbose_name='Категория')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фото в услугах'
        verbose_name_plural = 'Фото в услугах'


class ServChildren(models.Model):
    title = models.CharField(max_length=150, verbose_name='Назавние')
    h1 = models.CharField(max_length=200, verbose_name='Заголовок H1', null=True)
    breadcrumbs = models.ImageField(upload_to='serv', null=True, blank=True)
    image = models.ImageField(upload_to='servsildren')
    text = models.TextField(verbose_name='Описание')
    parent = models.ForeignKey(Serv, on_delete=models.CASCADE, related_name='children', verbose_name='Категория')
    meta_title = models.CharField(max_length=100, verbose_name='Мета заголовок')
    meta_description = models.CharField(max_length=280, verbose_name='Мета описание')
    meta_keywords = models.CharField(max_length=200, verbose_name='Ключевые слова')
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('servchildren_detail', kwargs={'parent': self.parent.slug, 'slug': self.slug})

    class Meta:
        verbose_name = 'Вложенная категория'
        verbose_name_plural = 'Вложенные категории'

class ServChildrenBlock(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заголовок', null=True, blank=True)
    text = models.TextField(verbose_name='Текст блока')
    color = models.CharField(max_length=20, verbose_name='Цвет фона')
    text_color = models.CharField(max_length=20, verbose_name='Цвет текста', null=True, blank=True)
    bg = models.ImageField(upload_to='remontblock', verbose_name='Фон', null=True, blank=True)
    parent = models.ForeignKey(ServChildren, on_delete=models.CASCADE, related_name='block', verbose_name='блок')
    button = models.CharField(max_length=150, verbose_name='Текст кнопки', null=True, blank=True)

    class Meta:
        verbose_name = 'Дополнительный блок'
        verbose_name_plural = 'Дополнительные блоки'



class Slider(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    description = models.CharField(max_length=500, verbose_name='Описание')
    parent = models.ForeignKey(Serv, on_delete=models.CASCADE, related_name='slider', verbose_name='Категория')
    image = models.ImageField(upload_to='sliders', verbose_name='Изображение', null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'


class Portfolio(models.Model):
    title = models.CharField(max_length=250, verbose_name='Назавние')
    breadcrumbs = models.ImageField(upload_to='portfolio', verbose_name='Хлебные крошки (картинка)')
    price = models.CharField(max_length=150, verbose_name='Цена')
    date = models.DateField(verbose_name='Дата окончания проекта')
    adress = models.CharField(max_length=250, verbose_name='Адрес объекта')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    meta_title = models.CharField(max_length=100, verbose_name='Мета заголовок', null=True)
    meta_description = models.CharField(max_length=280, verbose_name='Мета описание', null=True)
    meta_keywords = models.CharField(max_length=200, verbose_name='Ключевые слова', null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'


class PortfolioProperty(models.Model):
    title = models.CharField(max_length=150, verbose_name='Назавние')
    data = models.CharField(max_length=150, verbose_name='Значение')
    parent = models.ForeignKey(Portfolio, related_name='property', verbose_name='Проект', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'

class PortfolioImage(models.Model):
    image = models.ImageField(upload_to='portfolio')
    parent = models.ForeignKey(Portfolio, related_name='image', verbose_name='Изображение', on_delete=models.CASCADE)
    def __str__(self):
        return self.parent.title
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'



