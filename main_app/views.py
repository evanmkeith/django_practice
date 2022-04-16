from ast import Del
from ctypes import cast
from http.client import CannotSendHeader
from re import template
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Movie, Movie_Props
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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

@method_decorator(login_required, name='dispatch')
class Movie_Create(CreateView):
    model = Movie
    fields = '__all__'
    template_name = "movie_create.html"
    success_url = "/movies/"

    # def get_success_url(self): 
    #     return reverse('movie_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/movies')

class Movie_Detail(DetailView):
    model = Movie
    template_name = "movie_detail.html"

@method_decorator(login_required, name='dispatch')
class Movie_Update(UpdateView):
    model = Movie
    fields = ['img', 'title', 'genre', 'year', 'movieprops']
    template_name = "movie_update.html"
    # success_url = "/movies/"
    def get_success_url(self): 
        return reverse('movie_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class Movie_Delete(DeleteView):
    model = Movie
    template_name = "movie_delete_confirmation.html"
    success_url = "/movies/"

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    movies = Movie.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'movies': movies})

def movieprop_index(request):
    movieprops = Movie_Props.objects.all()
    return render(request,  'movieprop_index.html', {'movieprops': movieprops})

def movieprop_show(request, pk):
    movieprop = Movie_Props.objects.get(id=pk)
    return render(request, 'movieprop_show.html', {'movieprop': movieprop})

# class movieprop_show(DetailView): 
#     model = Movie_Props
#     template_name = "movieprop_show.html"

@method_decorator(login_required, name='dispatch')
class Movie_Prop_Create(CreateView):
    model = Movie_Props
    fields = '__all__'
    template_name = "movieprop_form.html"
    success_url = '/movieprop'

@method_decorator(login_required, name='dispatch')
class Movie_Prop_Update(UpdateView): 
    model = Movie_Props
    fields = ['name', 'use']
    template_name = "movieprop_update.html"
    success_url = '/movieprop'

@method_decorator(login_required, name='dispatch')
class Movie_Prop_Delete(DeleteView): 
    model = Movie_Props
    template_name = "movieprop_confirm_delete.html"
    success_url = '/movieprop/'

def signup_view(request): 
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            login(request, user)
            print("Hiya!", user.username)
            return HttpResponseRedirect('/user/'+str(user.username))
        else: 
            return render(request, 'signup.html', {'form': form})
    else: 
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/movies')

def login_view(request):
    # if post, then authenticate (user submitted username and password)
    if request.method == 'POST': 
        form = AuthenticationForm(request, request.POST)
        # form = LoginForm(request.POST)
        if form.is_valid(): 
            u = form.cleaned_data['username']
            p = form.cleaned_data['password'] 
            user = authenticate(username=u, password=p)
            if user is not None: 
                if user.is_active: 
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u) 
                else: 
                    print('The account has been disabled.')
                    return render(request, 'login.html', {'form': form})
            else: 
                print('The username and/or password is incorrect')
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'loging.html', {'form': form})
    else: # it was a get request so send the emtpy login form
        # form = LoginForm()
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    