from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    tel = models.CharField(max_length=20, verbose_name='Телефон')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name