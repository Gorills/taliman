# Generated by Django 3.1.7 on 2021-04-12 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0002_auto_20210411_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='serv',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='servchildren',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]