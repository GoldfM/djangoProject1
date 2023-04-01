# Generated by Django 4.1.7 on 2023-03-10 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Advertisment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('descript', models.TextField(verbose_name='Описание')),
                ('place', models.CharField(max_length=255, verbose_name='Локация')),
                ('timeCreated', models.TimeField(auto_now_add=True)),
                ('timeUpdate', models.TimeField(auto_now=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='advertisement.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['title', 'price'],
            },
        ),
    ]
