from django.db import models
from user.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=55)
    short_desc = models.CharField(max_length=256, blank=True)


    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    image = models.ImageField(upload_to="actors", blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Film(models.Model):
    name = models.CharField(max_length=55)
    image = models.ImageField(upload_to="films")
    description = models.TextField(blank=True)
    category_list = models.ManyToManyField(Category)
    actor_list = models.ManyToManyField(Actor)
    trailer = models.TextField(blank=True)
    year = models.DateField()

    def __str__(self):
        return self.name

class ListFavoriteFilmUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ManyToManyField(Film)

    def __str__(self):
        return self.user.username