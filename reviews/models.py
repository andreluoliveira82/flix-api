from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    """
    Permite a avaliação de um filme.
    """

    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name="reviews")
    stars = models.IntegerField(
        verbose_name="classifiação",
        validators=[
            MinValueValidator(0, message="A classificação deve ser maior ou igual a 0"),
            MaxValueValidator(5, message="A classificação deve ser menor ou igual a 5"),
        ],
    )

    comment = models.TextField(verbose_name="comentário", blank=True, null=True)

    def __str__(self):
        return self.movie
