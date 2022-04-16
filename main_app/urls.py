from django.urls import path, include
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
    path('movieprop/', views.movieprop_index, name='movieprop_index'),
    path('movieprop/<int:pk>', views.movieprop_show, name='movieprop_show'),
    path('movieprop/create/', views.Movie_Prop_Create.as_view(), name='movieprop_create'),
    path('movieprop/<int:pk>/update/', views.Movie_Prop_Update.as_view(), name='movieprop_update'),
    path('movieprop/<int:pk>/delete/', views.Movie_Prop_Delete.as_view(), name='movieprop_delete'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/signup/', views.signup_view, name='signup'),
]