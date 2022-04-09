from django.db import models

# Create your models here.
GENRE_CHOICES = (
    ("sci-fi", "sci-fi"), 
    ("adventure", "adventure"), 
    ("comedy", "comedy"), 
    ("romance", "romance"), 
    ("drama", "drama"), 
    ("documentary", "documentary")
)

class Movie(models.Model):
    
    img = models.CharField(max_length=250)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=15, choices = GENRE_CHOICES)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.title
    
    class Meta: 
        ordering = ['year']

