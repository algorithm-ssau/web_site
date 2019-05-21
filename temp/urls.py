from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('city/<city>', views.FilteredListView.as_view(), name='sights_in_city'),
    path('category/<category>', views.FilteredListView.as_view(), name='sights_of_category'),
    path('sight/<int:id>', views.sight_view, name='sight'),
    path('categories/', views.categories, name='categories'),
    path('search/', views.search, name='search'),
    path('cities/', views.cities, name='cities')
]