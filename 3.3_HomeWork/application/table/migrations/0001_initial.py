# Generated by Django 2.1.1 on 2018-11-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsvPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csvPath', models.CharField(max_length=200, verbose_name='Путь до файла csv')),
            ],
            options={
                'verbose_name': 'Путь к CSV',
                'verbose_name_plural': 'Путь к CSV',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_number', models.CharField(max_length=50, unique=True, verbose_name='Порядковый номер')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('width', models.CharField(max_length=50, verbose_name='Ширина')),
            ],
            options={
                'verbose_name': 'Поле таблицы',
                'verbose_name_plural': 'Поля таблицы',
            },
        ),
    ]
