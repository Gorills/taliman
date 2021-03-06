# Generated by Django 3.1.7 on 2021-05-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_contact_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('tel', models.CharField(max_length=20, verbose_name='Телефон')),
                ('message', models.TextField(verbose_name='Текст отзыва')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('moderate', models.BooleanField(default=False, verbose_name='Опубликован')),
            ],
        ),
    ]
