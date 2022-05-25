from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    data = {
        'movies': movies,
    }
    return render(request, 'movie_app/all_movies.html', data)

def info_about_movie(request, movie: str):
    info = get_object_or_404(Movie, slug=movie)
    return render(request,'movie_app/info_about_movie.html', context={
        'movie': info,
    })

def get_info_about_directors(request):
    data = {
        'directors': Director.objects.all()
    }
    return render(request, 'movie_app/info_about_directors.html', data)

def get_info_about_director(request, author):
    data = {
        'director': get_object_or_404(Director, slug=author)
    }
    return render(request, 'movie_app/info_about_director.html', data)

def get_info_about_actors(request):
    data = {
        'actors': Actor.objects.all()
    }
    return render(request, 'movie_app/info_about_actors.html', data)

def get_info_about_actor(request, actor):
    data = {
        'actor': get_object_or_404(Actor, slug=actor)
    }
    return render(request, 'movie_app/info_about_actor.html', data)


