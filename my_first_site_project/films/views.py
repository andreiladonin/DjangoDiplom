from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Film, Category, ListFavoriteFilmUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

def index(request):

    object_list = Film.objects.all()
    paginator = Paginator(object_list, 6)

    page = request.GET.get('page', 1)

    try:
        films = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        films = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        films = paginator.page(paginator.num_pages)

    context = {
        "title": "Главная страница",
        "categories": Category.objects.all(),
        "films": films
    }

    return render(request, "films/index.html", context)


def get_category(request, id):

    category = get_object_or_404(Category, pk=id)
    films = Film.objects.filter(category_list=category)

    context = {
        'title': category.name,
        "category": category,
        'films': films
    }

    return render(request, "films/category.html", context)


def get_film(request, id_film):

    if request.method == "POST":
        favorite_film = None
        try:
            favorite_film = ListFavoriteFilmUser.objects.get(user=request.user)
            film = Film.objects.get(id=request.POST['favorite_film'])
            favorite_film.film.add(film)
            favorite_film.save()
            return HttpResponseRedirect(reverse(f"films:film", args=[request.POST['favorite_film']]))
        except:
            favorite_film = ListFavoriteFilmUser.objects.create(user=request.user)
            film = Film.objects.get(id=request.POST['favorite_film'])
            favorite_film.film.add(film)
            favorite_film.save()
            return HttpResponseRedirect(reverse(f"films:film", args=[request.POST['favorite_film']]))

    film = get_object_or_404(Film, pk=id_film)

    is_favorite_film = False

    try:
        favorite_film = ListFavoriteFilmUser.objects.get(user=request.user, film=id_film)

        if favorite_film:
            is_favorite_film = True
    except:
        is_favorite_film = False

    context = {
        "title": f"{film.name}",
        "film": film,
        "is_favorite_film": is_favorite_film
    }

    return render(request, "films/film.html", context)


def favorite_film_user(request):
    favorite_films = ListFavoriteFilmUser.objects.get(user=request.user).film.all()
    print(favorite_films)
    context = {
        "title": "Избранные фильмы",
        "films": favorite_films
    }
    return render(request, "films/favorite.html", context)