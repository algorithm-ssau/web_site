from random import sample

from django.shortcuts import render
from django.views import generic
from .models import Post
from django.http import Http404
from django.db.models import F, Q

# Create your views here.
def index(request):
    """
    Функция отображения для главной страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_sights=Post.objects.all().count()
    popsightslist = Post.objects.order_by('-times_visited')
    most_visited=popsightslist.first().name
    mv_city = popsightslist.first().city
    random_sights = sample(set(popsightslist[:256]), 3)
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_sights':num_sights, 'most_visited':most_visited, 'mv_city':mv_city, 'image1':random_sights[0].postimage_set.first(), 'image2':random_sights[1].postimage_set.first(), 'image3':random_sights[2].postimage_set.first(), 'sight1':random_sights[0], 'sight2':random_sights[1], 'sight3':random_sights[2]}
    )

def categories(request):
    '''
    Список категорий
    '''
    return render(
        request,
        'cats.html'
    )

def cities(request):
    '''
    Список городов
    '''
    return render(
        request,
        'cities.html'
    )

def search(request):
    '''
    Отображает список 20 наиболее популярных достопримечательностей, соответствующих запросу
    '''
    search_query3 = request.GET.get('q', '').strip(',- ').lower()
    search_query2 = search_query3.split(',')
    search_query1 = []
    search_query = []
    for str in search_query2:
        search_query1.extend(str.split('-'))
    for str in search_query1:
        search_query.extend(str.split(' '))
    # четырех слов хватит
    laststr = search_query[len(search_query)-1]
    for i in range(len(search_query), 4):
        search_query.append(laststr)
    if search_query[0] == '':
        return render(
            request,
            'search.html',
            context={'sights_list': 'Ваш запрос пуст',}
        )
    # SQLite не поддерживает регистронезависимый поиск по кириллице, поэтому icontains бесполезен
    init_list = list(Post.objects.all().order_by('-times_visited'))
    filtered_list = []
    for sight in init_list:
        sightwordslist1 = sight.name.lower().split('-')
        sightwordslist = []
        for str in sightwordslist1:
            sightwordslist.extend(str.split(' '))
        if not set(search_query).isdisjoint(set(sightwordslist)):
            filtered_list.append(sight)
    return render(
        request,
        'search.html',
        context={'sights_list': filtered_list, 'search_query':search_query3}
    )

def sight_view(request,id):
    '''
    Отображает подробную информацию о выбранной достопримечательности
    '''
    try:
        sight=Post.objects.get(pk=id)
        sight.times_visited = F('times_visited')+1
        sight.save()
        first_image = sight.postimage_set.first()
        images_list = list(sight.postimage_set.all())[1:]
        image_pairs = [(images_list[2*k], images_list[2*k+1]) for k in range(len(images_list)//2)]
        if len(images_list)%2 == 1:
            image_pairs.append((images_list[len(images_list)-1], False))
    except Post.DoesNotExist:
        raise Http404("Запрошенной достопримечательности не существует")
    return render(
        request,
        'sight.html',
        context={'sight': sight, 'first_image': first_image, 'other_images': image_pairs}
    )

class FilteredListView(generic.ListView):
    """
    Отображает список 20 наиболее популярных достопримечательностей выбранной категории
    либо достопримечательности в конкретном городе
    """
    model = Post
    template_name = 'search.html'
    def get_queryset(self):
        if 'city' in self.kwargs:
            filtered_list = Post.objects.filter(city__iexact=self.kwargs['city'])
        else:
            filtered_list = Post.objects.filter(type__iexact=self.kwargs['category'])
        return filtered_list.order_by('-times_visited')[:20]
    def get_context_data(self, **kwargs):
        context = super(FilteredListView, self).get_context_data(**kwargs)
        if 'city' in self.kwargs:
            context['city'] = self.kwargs['city']
        return context
