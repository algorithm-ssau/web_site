
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
        ('d', 'Музеи'),
        ('e', 'Театры'),
        ('f', 'Улицы, площади'),
        ('g', 'Парки')
    )
    
    name = models.CharField(max_length=200) 
    text = models.TextField()   # описание
    city = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=SIGHT_TYPES)
    times_visited = models.IntegerField()
    def __str__(self):
        return self.name


