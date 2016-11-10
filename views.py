from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Movie


def index(request):
    return render(request, 'index.html')


class MovieList(ListView):
    template_name = 'core/movie_list.html'
    model = Movie
    context_object_name = 'movies'

    def get_queryset(self):
        m = Movie.objects.all()

        if self.request.GET.get('great_movie', False):
            q = Movie.objects.all().aggregate(Max('raised'))
            m = Movie.objects.filter(raised=q['raised__max'])
        return m


class MovieDetail(DetailView):
    template_name = 'core/movie_detail.html'
    model = Movie


class MovieCreate(CreateView):
    template_name = 'core/movie_form.html'
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('core:movie_list')