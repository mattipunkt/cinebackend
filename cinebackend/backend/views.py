import urllib.request
from django.shortcuts import render, redirect
from . import utils
import itertools
import datetime
from . import models, forms
import urllib


# Create your views here.
def index(request):
    return render(request, "base.html")


def moviemanager(request):
    return render(request, "moviemanager.html", {
        "movies": models.Movie.objects.all(),
    })


def addmovie(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        tmdb_id = request.POST.get("tmdb_id")
        director = request.POST.get("director")
        actors = str()
        for actor in utils.credit_request(tmdb_id)["cast"]:
            if request.POST.get(str(actor['id']), None) is not None:
                if actors == "":
                    actors = str(actor["name"])
                else:
                    actors = actors + ', ' + str(actor["name"])
        year = request.POST.get("year")
        description = request.POST.get("description")
        poster_path = utils.movie_request(tmdb_id)["poster_path"]
        models.Movie.objects.create(title=title, tmdb_filled=True, tmdb_id=tmdb_id, year=year, description=description, actors=actors, director=director, cover_url="https://image.tmdb.org/t/p/original" + poster_path)
        return redirect('/cinebackend')

    else:
        return render(request, "addmovie/addmovie.html")


def tmdbsearch(request):
    query = request.GET.get('q')
    print("Making TMDB Request: " + query)
    results = utils.tmdb_requests(query)
    results = results['results']
    return render(request, "addmovie/searchresults.html", {"results": results,})

def movieedit(request):
    tmdb = request.GET.get("tmbd")
    tmdb_id = request.GET.get("tmbd_id")
    title = request.GET.get("title")
    release_date = request.GET.get("release-date")
    tmdb_request = utils.credit_request(tmdb_id)
    director = tmdb_request["crew"][0]["name"]
    actors = tmdb_request["cast"]
    description = utils.movie_request(tmdb_id)["overview"]
    return render(request, "addmovie/movieedit.html", {
        "tmdb": tmdb,
        "tmdb_id": tmdb_id,
        "title": title,
        "release_date": release_date,
        "director": director,
        "actors": actors,
        "year": datetime.datetime.strptime(release_date, "%Y-%m-%d").year,
        "description": description
    })


def editmovie(request, id):
    if request.method == 'GET':
        movie = models.Movie.objects.get(pk=id)
        return render(request, "addmovie/edit_exisiting_movie.html", {
            "movie": movie,
        })
    if request.method == 'POST':
        movie = models.Movie.objects.get(pk=id)
        movie.title = request.POST.get('title')
        active = request.POST.get('active', 'false')
        if active != 'false':
            active = True
        else: active = False
        movie.active = active
        movie.director = request.POST.get('director')
        movie.actors = request.POST.get('actors')
        movie.year = request.POST.get('year')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('/cinebackend/moviemanager')
    

def changecover(request, id):
    if request.method == "POST":
        movie = models.Movie.objects.get(pk=id)
        movie.cover_url = "https://image.tmdb.org/t/p/original" + request.POST.get("cover_url")
        movie.save()
        return redirect('/cinebackend/moviemanager')
    elif request.method == "GET":
        movie = models.Movie.objects.get(pk=id)
        return render(request, "addmovie/cover_selection.html", {
            "movie": movie,
            "covers": utils.cover_request(movie.tmdb_id)["posters"],
        })  


def scheduler(request):
    if request.method == "GET":
        movies = models.Movie.objects.all()
        times_dict = list()
        for movie in movies:
            times_dict.append(
                {
                    "movie": movie,
                    "times": models.Showtimes.objects.all().filter(movie=movie),
                }
            )
        return render(request, "scheduling/main.html", {
            "selectionform": forms.NewTimeForm,
            "movies":times_dict,
        })


def addtime(request, id):
    if request.method == "POST":
        movie = models.Movie.objects.get(pk=id)
        time = request.POST.get('time')
        date = request.POST.get('date')
        # datett = datetime.datetime.strptime()
        new_time = models.Showtimes.objects.create(
            date = date,
            time = time,
            movie = movie,
            language = request.POST.get('language'),
            location = request.POST.get('location'),
            premiere = request.POST.get('premiere'),
        )
        return redirect('/cinebackend/scheduler')