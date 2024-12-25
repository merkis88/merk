from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about' ),
    path('promo/', views.promo, name='promo' ),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegistrationUser.as_view(), name='register'),
    path('booking/', views.BookingCreateView.as_view(), name='booking'),
    path('profile/', views.Profile.as_view(), name='profile')
]
