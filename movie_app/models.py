from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Star(models.Model):
    stars = models.IntegerField(default=1)

    def __str__(self):
        return str(self.stars)
class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(default=0)




    def director_str(self):
        if self.director:
            return self.director.name
        return None

    def __str__(self):
        return self.title

    def get_avg_rating(self):
        avg_rating = self.movie_reviews.aggregate(avg_rating=Avg('stars__stars'))['avg_rating']
        return avg_rating or 0.0






class Review(models.Model):

    text = models.CharField(max_length=200, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_reviews')
    stars = models.ForeignKey(Star, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return str(self.text)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.movie.rating = self.movie.movie_reviews.aggregate(Avg('stars'))['stars__avg']
    #     self.movie.save()