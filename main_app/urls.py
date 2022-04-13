from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('movies/', views.Index.as_view(), name="index"), 
    path('about/', views.About.as_view(), name="about"),
    path('movies/new/', views.Movie_Create.as_view(), name="movie_create"),
    path('movies/<int:pk>/', views.Movie_Detail.as_view(), name="movie_detail"),
    path('movies/<int:pk>/update', views.Movie_Update.as_view(), name="movie_update"), 
    path('movies/<int:pk>/delete', views.Movie_Delete.as_view(), name="movie_delete"),
    path('user/<username>', views.profile, name='profile'),
    
]