from ctypes import cast
from http.client import CannotSendHeader
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Movie

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
        context["movies"] = Movie.objects.all()
        return context 

class Home(TemplateView): 
    template_name = "home.html"

class About(TemplateView): 
    template_name = "about.html"

