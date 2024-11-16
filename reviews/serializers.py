from rest_framework import serializers
from reviews.models import Review


class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        """
        docstring
        """

        model = Review
        fields = "__all__"

    # validates
    # por definição todas as validações devem começar com validate_ seguido do nome do campo

    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("A nota deve estar entre 1 e 5")
        return value
