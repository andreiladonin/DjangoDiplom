from django.urls import path, include
from . import views


app_name = "films"

urlpatterns = [
    path('', views.index, name="index"),
    path('film/<int:id_film>', views.get_film, name="film"),
    path('category/<int:id>', views.get_category, name="category"),
    path('favorite_user/', views.favorite_film_user, name="favoriteuser")

]