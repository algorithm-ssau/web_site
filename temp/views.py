from django.shortcuts import render
from django.views import generic
from .models import Post
from django.http import Http404
from django.db.models import F

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
def sight_view(request,id):
    try:
        sight=Post.objects.get(pk=id)
        sight.times_visited = F('times_visited')+1
        sight.save()
    except Post.DoesNotExist:
        raise Http404("Запрошенной достопримечательности не существует")
    return render(
        request,
        'sight.html',
        context={'sight': sight}
    )
class FilteredListView(generic.ListView):
    """
    Отображает список достопримечательностей в конкретном городе.
    """
    model = Post

    def get_queryset(self):
        # пока фильтр только по городу; когда появятся формы, можно будет добавить другие критерии
        filtered_list = Post.objects.filter(city__iexact=self.kwargs['city'])
        return filtered_list

    def get_context_data(self, **kwargs):
        context = super(FilteredListView, self).get_context_data(**kwargs)
        context['city'] = self.kwargs['city']
        return context
