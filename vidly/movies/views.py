from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    #output = ', '.join([m.title for m in movies])
    #return HttpResponse(output)
    return render(request, 'movies/index.html', {'movies': movies})

    # # SELECT * FROM movies_movie
    # Movie.objects.filter(release_year=1964)
    # # SELECT * FROM movies_movie WHERE release_year=1964
    # Movie.objects.get(id=1)
    # return HttpResponse("Hello World")

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', { 'movie': movie })
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     return render(request, 'movies/detail.html', { 'movie': movie })
    # except Movie.DoesNotExist:
    #     raise Http404()