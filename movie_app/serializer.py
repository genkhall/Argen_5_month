from rest_framework import serializers
from movie_app.models import *
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    def get_movies_count(self, director):
        return director.movie_set.count()

    class Meta:
        model = Director
        fields = 'name movies_count'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ' text stars movie_id'.split()


class MovieSerializerWithReview(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(many=True)
    director_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title description duration  director_name movie_reviews  '.split()

    def get_director_name(self, movie):
        return movie.director.name


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title description duration director'.split()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField()


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, category_id):
        try:
            Director.objects.get(id=category_id)
        except Director.DoesNotExist:
            raise ValidationError('No director with such id!')
        return category_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField(min_value=1)
    stars_id = serializers.IntegerField(min_value=1, max_value=5)

    def validate_movie_id(self, id):
        try:
            Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            raise ValidationError("No movie:(")
        return id

    def validate_stars_id(self, id):
        try:
            Star.objects.get(id=id)
        except Star.DoesNotExist:
            raise ValidationError("No star:(")
        return id
