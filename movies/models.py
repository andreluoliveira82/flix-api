from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    """Armazena dados sobre os filmes"""

    title = models.CharField(verbose_name="título", max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="movies")
    release_year = models.IntegerField(verbose_name="ano de lançamento")
    director = models.CharField(verbose_name="diretor", max_length=100)
    duration = models.IntegerField(verbose_name="duração (minutos)")
    actors = models.ManyToManyField(Actor, related_name="actors")

    def __str__(self):
        return self.title.capitalize()
