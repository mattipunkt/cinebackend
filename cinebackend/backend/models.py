from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    active = models.BooleanField(default=False)
    title = models.CharField(default="kein titel gegeben", max_length=120)
    tmdb_filled = models.BooleanField(default=False)
    tmdb_id = models.IntegerField(default="00000")
    year = models.CharField(default="0000", max_length=4)
    description = models.CharField(default="keine beschreibung angegeben", max_length=2000)
    actors = models.CharField(default="Keine Schauspieler angegeben", max_length=120)
    director = models.CharField(default="Kein regisseur angegeben", max_length=100)
    use_in_carousel = models.BooleanField(default=False)
    cover_url = models.CharField(default="", max_length=2000)

class Showtimes(models.Model):
    time = models.TimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    collection = models.CharField(null=True, max_length=100)
    language = models.CharField(default="dt. OV", max_length=100)
    location = models.CharField(default="", max_length=100)
    premiere = models.BooleanField(default=False)
