from django.contrib import admin
from .models import Category, Actor, Film, ListFavoriteFilmUser

# Register your models here.
admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Film)
admin.site.register(ListFavoriteFilmUser)