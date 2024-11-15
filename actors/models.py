from django.db import models

COUNTRIES = (
    ("USA", "Estados Unidos"),
    ("UK", "Reino Unido"),
    ("JP", "Japão"),
    ("BR", "Brasil"),
    ("DE", "Alemanha"),
    ("FR", "França"),
    ("IT", "Itália"),
    ("MX", "México"),
    ("PT", "Portugal"),
    ("ES", "Espanha"),
)

GENDERS = (
    ("M", "Masculino"),
    ("F", "Feminino"),
)


class Genre(models.Model):
    name = models.CharField(verbose_name="nome", max_length=50, unique=True)
    country = models.CharField(verbose_name="país", max_length=3, choices=COUNTRIES)


class Actor(models.Model):
    name = models.CharField(verbose_name="nome", max_length=50, unique=True)
    gender = models.CharField(verbose_name="sexo", max_length=1, choices=GENDERS)
    birthday = models.DateField(
        verbose_name="data de nascimento", null=True, blank=True
    )
    nationality = models.CharField(
        verbose_name="nacionalidade",
        max_length=50,
        choices=COUNTRIES,
        null=True,
        blank=True,
    )
    biography = models.TextField(verbose_name="biografia", null=True, blank=True)

    def __str__(self):
        return self.name.capitalize()
