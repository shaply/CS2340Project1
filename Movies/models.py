from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=255)
    rating = models.IntegerField(choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie.title