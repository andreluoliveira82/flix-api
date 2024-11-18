from django.db import models


class Genre(models.Model):
    name = models.CharField(verbose_name="gênero", max_length=50, unique=True)

    def __str__(self):
        return self.name.capitalize()
