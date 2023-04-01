from django.db import models
from django.urls import reverse


# Create your models here.
class Advertisment(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    price = models.IntegerField(verbose_name='Цена')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    descript = models.TextField(verbose_name='Описание')
    place = models.CharField(max_length=255, verbose_name='Локация')
    timeCreated = models.TimeField(auto_now_add= True)
    timeUpdate = models.TimeField(auto_now= True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('item', kwargs={'name':self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['title', 'price']

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']