import re
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout
from django.contrib import auth
from django.urls import reverse
from .forms import RegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.

TEMPLATE_PHONE = r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"


def account(request):
    return HttpResponse('account page')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST, files=request.FILES)

        if re.fullmatch(TEMPLATE_PHONE, request.POST['phone']) is None:
            return render(request, 'user/register.html',
                          {'title': "Регистрация", "errors": "Номер телеона не соотвествует шаблону", "form": form})
        else:
            if request.POST["password1"] == request.POST['password2']:
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse("users:login"))
                else:
                    return render(request, 'user/register.html', {"form": form, 'title': "Регистрация"})
            else:
                return render(request, 'user/register.html', {'title': "Регистрация", "errors": "Пароли не совпадают", "form": form})

    else:
        form = RegistrationForm()
    context = {
        'title': "Регистрация",
        'form': form
    }

    return render(request, 'user/register.html', context)


def login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("films:index"))
        else:
            return render(request, "user/login.html",
                          {'title': 'Вход', 'form': UserLoginForm(), 'errors': "Неверный логин или пароль"})
    context = {
        "title": "Вход",
        "form": UserLoginForm()
    }

    return render(request, "user/login.html", context)

@login_required()
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse("films:index"))
