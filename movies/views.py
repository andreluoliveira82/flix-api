from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieModelSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    """Permite criar e exibir os filmes cadastrados em formato json."""

    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Exibe detalhes de um determinado filme, e permite a atualizacao e delecao do filme especificado"""

    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
