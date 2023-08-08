"""
URL configuration for Afisha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.directors_list_api_view),
    path('api/v1/directors/<int:d_id>/', views.detail_director_api_view, name='movie_review_list_api'),
    path('api/v1/movies/reviews/',views.movie_and_review_list_api_view),
    path('api/v1/movies/reviews/<int:movie_id>/', views.movie_review_detail_api_view),
    path('api/v1/movies/',views.movie_list_api_view),
    path('api/v1/movies/<int:movie_id>/', views.movie_detail_api_view),
    path('api/v1/reviews/',views.review_list_api_view),
    path('api/v1/reviews/<int:review_id>/', views.review_detail_api_view),
    path('api/v1/users/', include('users.urls'))

]
