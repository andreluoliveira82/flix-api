from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        """
        serializa e devolve todos os campos da model Movie
        """

        model = Movie
        fields = "__all__"
