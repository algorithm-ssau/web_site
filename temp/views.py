from random import sample

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
    num_sights=Post.objects.all().count() #
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
    return render(
        request,
        'cats.html'
    )
def sight_view(request,id):
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
