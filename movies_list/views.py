from django.shortcuts import render
from .models import Movie


def movie_list(request):
    genre = request.GET.get('genre')
    if genre:
        movies = Movie.objects.filter(genre=genre)
    else:
        movies = Movie.objects.all()

    genres = Movie.objects.values_list('genre', flat=True).distinct()
    return render(request, 'index.html', {'movies': movies, 'genres': genres})
