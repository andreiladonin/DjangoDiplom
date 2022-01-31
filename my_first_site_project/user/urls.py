from django.urls import path, include
from . import views


app_name = "users"

urlpatterns = [
    path('account', views.account, name="account"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout_user, name='logout')
]
