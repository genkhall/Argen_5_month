from django.shortcuts import render
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from movie_app.serializer import DirectorSerializer,MovieSerializer,ReviewSerializer
from movie_app.models import Director,Movie,Review
from rest_framework.renderers import JSONRenderer


@api_view(['GET'])
def directors_list_api_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(instance=directors, many=True).data
    return Response(data=data)

@api_view(['GET'])
def detail_director_api_view(request, d_id):
    try:
        directors = Director.objects.get(id=d_id)
    except Director.DoesNotExist:
        return Response(data={'message': 'No director '},
                        status=404)
    data = DirectorSerializer(instance=directors, many=False).data
    return Response(data=data)

@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(instance=movies, many=True).data
    return Response(data=data)

@api_view(['GET'])
def movie_detail_api_view(request,movie_id):
    try:
        movies = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response(status=404)
    data = MovieSerializer(instance=movies,many=False).data
    return Response(data=data)

@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(instance=reviews, many=True).data
    return Response(data=data)

@api_view(['GET'])
def review_detail_api_view(request, review_id):
    try:
        reviews = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(status=404)
    data = ReviewSerializer(instance=reviews, many=False).data
    return Response(data=data)
