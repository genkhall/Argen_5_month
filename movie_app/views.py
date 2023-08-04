from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from movie_app.serializer import DirectorSerializer, MovieSerializerWithReview, ReviewSerializer, \
    MovieSerializer,DirectorValidateSerializer,MovieValidateSerializer, ReviewValidateSerializer
from movie_app.models import Director, Movie, Review
from rest_framework.renderers import JSONRenderer
from django.db.models import Avg


@api_view(['GET', 'POST'])
def directors_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(instance=directors, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=400,
                            data=serializer.errors)
        name = serializer.validated_data.get("name")

        directors = Director.objects.create(
           name=name
        )
        return Response(data=DirectorSerializer(directors).data)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_director_api_view(request, d_id):
    try:
        directors = Director.objects.get(id=d_id)
    except Director.DoesNotExist:
        return Response(data={'message': 'No director '},
                        status=404)
    if request.method == 'GET':
        data = DirectorSerializer(instance=directors, many=False).data
        return Response(data=data)
    elif request.method == "PUT":
        serializer = DirectorSerializer(instance=directors,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    else:

        directors.delete()
        return Response(status=204)


@api_view(['GET'])
def movie_and_review_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializerWithReview(movies, many=True)

        avg_rating = Review.objects.aggregate(avg_rating=Avg('stars__stars'))['avg_rating']

        response_data = {
            'movies': serializer.data,
            'average_rating': avg_rating
        }
        return Response(response_data)


@api_view(['GET'])
def movie_review_detail_api_view(request, movie_id):
    try:
        movies = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response(status=404)
    data = MovieSerializerWithReview(instance=movies, many=False).data
    return Response(data=data)


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        data = MovieSerializer(instance=movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400, data=serializer.errors)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')

        try:
            director = Director.objects.get(pk=director_id)
        except Director.DoesNotExist:
            return Response({'message': 'no director'}, status=404)

        movies = Movie.objects.create(
            title=title, description=description, duration=duration,director=director
        )
        movies.save()
        return Response(data=MovieSerializer(movies).data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, movie_id):
    try:
        movies = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response(status=404)
    if request.method == 'GET':
        data = MovieSerializer(instance=movies, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':


        serializer = MovieSerializer(instance=movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    else:
        movies.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        data = ReviewSerializer(instance=reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400,data=serializer.errors)

        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        stars_id = serializer.validated_data.get('stars_id')

        reviews = Review.objects.create(
            text=text, movie_id=movie_id, stars_id=stars_id
        )
        reviews.save()
        return Response(data=ReviewSerializer(reviews).data)



@api_view(['GET','PUT','DELETE'])
def review_detail_api_view(request, review_id):
    try:
        reviews = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(status=404)
    if request.method == "GET":
        data = ReviewSerializer(instance=reviews, many=False).data
        return Response(data=data)
    elif request.method == "PUT":

        serializer = ReviewSerializer(instance=reviews, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    else:
        reviews.delete()
        return Response(status=204)

