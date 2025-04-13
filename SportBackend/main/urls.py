from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('male-standards/', views.male_standards, name='male_standards'),
    path('female-standards/', views.female_standards, name='female_standards'),
    path('disciplines/', views.disciplines, name='disciplines'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
] 