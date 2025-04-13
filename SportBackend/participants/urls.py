from django.urls import path
from . import views

urlpatterns = [
    path('', views.participants_list, name='participants_list'),
    path('registration/', views.registration, name='registration'),
    path('api/register/', views.register_participant, name='register_participant'),
] 