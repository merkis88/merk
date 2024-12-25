from datetime import timezone
from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView
from .models import Car
from .forms import RegisterUserForm, LoginForm, BookingForm


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def promo(request):
    return render(request, 'promo.html')

class RegistrationUser(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

class LoginUser(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')
    template_name = 'login.html'

class BookingCreateView(LoginRequiredMixin, CreateView):
    form_class = BookingForm
    success_url = reverse_lazy('booking')
    template_name = 'booking.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Устанавливаем текущего пользователя
        form.instance.entry_time = timezone.now()  # Устанавливаем текущее время
        return super().form_valid(form)


class Profile(LoginRequiredMixin, View):
    extra_context = {'title': "Профиль"}

    def get(self, request, *args, **kwargs):
        user = request.user # Получаем текущего аутентифицированного пользователя
        cars = Car.objects.filter(owner=user) # Получаем все машины, связанные с пользователем
        context = {
            'user' : user,
            'cars' : cars,
        }
        return render(request, 'profile.html', context)
