from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import User


def is_there_an_email(value):
    try:
        user = User.objects.get(email=value)
        if user:
            return True
    except:
        return False


class RegistrationForm(UserCreationForm):
    CHOICES = [('мужской', 'мужской'),
               ('женский', 'женский')
                ]

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введиите  логин', 'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введиите имя', 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введиите фамилилию', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Введиите email', 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'class': 'form-control'}))
    sex = forms.ChoiceField(choices=CHOICES, label="Пол", widget=forms.RadioSelect(attrs={"class": "form-check-input "}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введиите номер телефона', 'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password1 = self.cleaned_data.get('password1')
        if is_there_an_email(email):
            raise forms.ValidationError('Email уже занят')
        try:
            validate_password(password1, self.instance)
        except forms.ValidationError as error:
            raise forms.ValidationError('Пароль не соотвествует шаблону')

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  'sex',
                  'phone',
                  'image',)


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введиите  логин', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')