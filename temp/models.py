
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse #Used to generate URLs by reversing the URL patterns


class Post(models.Model):
    """
    Информация о туристическом объекте.
    """
    SIGHT_TYPES = (
        ('a', 'Классическая архитектура'), # до 1940-50-х
        ('b', 'Современная архитектура'),
        ('c', 'Скульптура'),
        ('d', 'Музеи, выставки и галереи'),
        ('e', 'Театры'),
        ('f', 'Улицы, площади'),
        ('g', 'Природные объекты'), # "Природа"
        ('h', 'Развлечения')
    )
    
    name = models.CharField('Название', max_length=200) 
    city = models.CharField('Город', max_length=50)
    text = models.TextField('Описание')
    more_text = models.TextField('Подробное описание', blank=True)
    address = models.CharField('Адрес', blank=True, max_length=200)
    opening_hours = models.CharField('Режим работы', blank=True, max_length=200)
    phone = models.CharField('Телефон', blank=True, max_length=200)
    website = models.CharField('Сайт', blank=True, max_length=200)
    map_data = models.TextField('Карта', blank=True)
    type = models.CharField('Вид', max_length=1, choices=SIGHT_TYPES)
    times_visited = models.IntegerField()
    class Meta:
        ordering = ['city', 'type'] # либо ['times_visited']
        verbose_name = 'Достопримечательность'
    def get_absolute_url(self):
        return reverse('sight', args=[str(self.id)])
    def __str__(self):
        return self.name

class PostImage(models.Model):
    """
    Изображение (фотография) туристического объекта.
    У достопримечательности может быть (и, как правило, будет) больше одной фотографии.
    """
    sight = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name="Достопримечательность")
    image = models.ImageField('Изображение', upload_to='images/%Y/%m/%d/')
    class Meta:
        verbose_name = 'Фото'
    def __str__(self):
        return '{}'.format(self.id)

