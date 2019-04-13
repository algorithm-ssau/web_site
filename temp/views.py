from django.shortcuts import render
from django.views import generic
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
class CityListView(generic.ListView):
    """
    Отображает список достопримечательностей в конкретном городе.
    """
    model = Post

    def get_queryset(self):
        return Post.objects.filter(city__iexact=self.kwargs['city'])
    def get_context_data(self, **kwargs):
        context = super(CityListView, self).get_context_data(**kwargs)
        context['city'] = self.kwargs['city']
        return context
   
