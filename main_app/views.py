from ctypes import cast
from http.client import CannotSendHeader
from re import template
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Movie
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, UpdateView
from django.urls import reverse

# Fake-a-base Movies
# class Movie: 
#     def __init__(self, title, genre, year): 
#         self.title = title
#         self.genre = genre
#         self.year = year

# movies = [
#     Movie("The Abyss", "sci-fi", 1989), 
#     Movie("Indiana Jones: Raiders of the Lost Ark", "adventure", 1981), 
#     Movie("2001: A Space Odyssey ", "sci-fi", 1968), 
#     Movie("Interstellar", "sci-fi", 2014), 
#     Movie ("The Matrix", "sci-fi", 1999)
# ]
#End fake-a-base

# Create your views here.
class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")

        if title != None: 
            context["movies"] = Movie.objects.filter(title__icontains=title)
            context["header"] = f"Searching for {title}"
        else: 
            context["movies"] = Movie.objects.all()
            context["header"] = "Movies:"

        return context 

class Home(TemplateView): 
    template_name = "home.html"

class About(TemplateView): 
    template_name = "about.html"

class Movie_Create(CreateView):
    model = Movie
    fields = ['img', 'title', 'genre', 'year']
    template_name = "movie_create.html"
    #success_url = "/movies/"
    def get_success_url(self): 
        return reverse('movie_detail', kwargs={'pk': self.object.pk})

class Movie_Detail(DetailView):
    model = Movie
    template_name = "movie_detail.html"

class Movie_Update(UpdateView):
    model = Movie
    fields = ['img', 'title', 'genre', 'year']
    template_name = "movie_update.html"
    # success_url = "/movies/"
    def get_success_url(self): 
        return reverse('movie_detail', kwargs={'pk': self.object.pk})