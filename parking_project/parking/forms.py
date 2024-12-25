from cProfile import label
from datetime import timezone

from django import forms
from django.contrib.admin.helpers import ActionForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User, Car


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    username = forms.CharField(label='Имя', error_messages={'required': 'Введите имя пользователя'} )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class BookingForm(forms.ModelForm):
    brand = forms.CharField(label='Марка машины')
    parking_fee = forms.DecimalField(label="Стоимость стоянки")
    entry_time = forms.DateTimeField(label='Дата и время въезда', initial=timezone.now)

    class Meta:
        model = Car
        fields = ['brand', 'parking_fee', 'entry_time']