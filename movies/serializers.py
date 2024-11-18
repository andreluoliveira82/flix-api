from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    # campo calculado (nao existe no database) para retornar a classificação média do filme, de acordo com as avaliações (reviews)
    rate = serializers.SerializerMethodField(read_only=True)
    reviews_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """
        serializa e devolve todos os campos da model Movie
        """

        model = Movie
        fields = "__all__"

    # campos calcualdos no serializrer
    def get_rate(self, obj):
        """
        calcula a classificação média do filme com base nas avaliações (reviews)
        """
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]

        if rate:
            return round(rate, 1)

        return None

        # if reviews:
        #     ttl_stars = 0

        #     for review in reviews:
        #         ttl_stars += review.stars

        #     return round(ttl_stars / reviews.count(), 1)

        # return None

    def get_reviews_count(self, obj):
        """
        calcula a quantidade de avaliações (reviews) do filme
        """
        return obj.reviews.count() if obj.reviews else 0

    # ============================ validates ===================================
    # por definição todas as validações devem começar com validate_ seguido do nome do campo

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "O título deve ter pelo menos 3 caracteres"
            )
        return value

    def validate_release_year(self, value):
        if value < 1900:
            raise serializers.ValidationError(
                "O ano de lançamento deve ser maior ou igual a 1900"
            )
        return value

    # def validate_director(self, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("O nome do diretor deve ter pelo menos 3 caracteres")
    #     return value
    # def validate_genre(self, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("O gênero deve ter pelo menos 3 caracteres")
    #     return value
    # def validate_description(self, value):
    #     if len(value) < 10:
    #         raise serializers.ValidationError("A descrição deve ter pelo menos 10 caracteres")
    #     return value
