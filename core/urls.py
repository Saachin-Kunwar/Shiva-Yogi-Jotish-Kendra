from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.book_consultation, name='booking'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]