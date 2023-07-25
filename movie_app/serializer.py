from rest_framework import serializers
from movie_app.models import *


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    def get_movies_count(self,director):
        return director.movie_set.count()
    class Meta:
        model = Director
        fields = 'name movies_count'.split()




class ReviewSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = Review
        fields = ' text stars'.split()

class MovieSerializerWithReview(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(many=True)
    director_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title description duration  director_name movie_reviews  '.split()

    def get_director_name(self,movie):
        return movie.director.name


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title description duration director'.split()