from django.db.models import Avg, Count
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPermission
from movies.models import Movie
from .serializers import (
    MovieModelSerializer,
)
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    """Permite criar e exibir os filmes cadastrados em formato json."""

    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Movie.objects.all()
    # serializer_class = MovieModelSerializer
    #
    # Este trecho acima (comentado) seria é o serializer padrão,
    # mas vamos usar o metodo abaixo para mudar o comportamento de acordo com o request
    # e assim formatar os dados de acordo com o request

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Exibe detalhes de um determinado filme, e permite a atualizacao e delecao do filme especificado"""

    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieStatsView(views.APIView):
    """Exibe estatisticas dos filmes cadastrados"""

    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )

    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values("genre__name").annotate(
            count=Count(("id"))
        )
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg("stars"))["avg_stars"]

        return response.Response(
            data={
                "total_movies": total_movies,
                "movies_by_genre": movies_by_genre,
                "total_reviews": total_reviews,
                "average_stars": round(average_stars, 1) if average_stars else 0,
            },
            status=status.HTTP_200_OK,
        )
