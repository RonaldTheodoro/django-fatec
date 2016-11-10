from django.conf.urls import url
from .views import index
from .views import MovieList
from .views import MovieDetail
from .views import MovieCreate


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^movie/$', MovieList.as_view(), name='movie_list'),
    url(r'^movie/(?P<pk>\d+)/$', MovieDetail.as_view(), name='movie_detail'),
    url(r'^movie/add/$', MovieCreate.as_view(), name='movie_add'),
]