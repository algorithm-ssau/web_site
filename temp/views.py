from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    """
    Функция отображения для главной страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_sights=Post.objects.all().count()
    
    # Доступные книги (статус = 'a')
    most_visited=Post.objects.order_by('-times_visited').first().name
    mv_city = Post.objects.order_by('-times_visited').first().city
    
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_sights':num_sights, 'most_visited':most_visited, 'mv_city':mv_city}
    )