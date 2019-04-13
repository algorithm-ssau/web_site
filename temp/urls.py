from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('city/<city>', views.CityListView.as_view(), name='city_list'),
    path('sight/<int:id>', views.sight_view, name='sight')
]