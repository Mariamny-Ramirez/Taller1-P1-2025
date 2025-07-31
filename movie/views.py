from django.shortcuts import render
from django.http import HttpResponse
from unidecode import unidecode

from .models import Movie

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        normalized_term = unidecode(searchTerm.lower())
        all_movies = Movie.objects.all()
        movies = [movie for movie in all_movies if normalized_term in unidecode(movie.title.lower())]
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {
    'searchTerm': searchTerm,
    'movies': movies,
    'name': 'Mariamny Ramírez'
    })


def about(request):
    return render(request, 'about.html')