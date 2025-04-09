from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_card, name='add_card'),
    path('cards/', views.card_list, name='card_list'),
    path('practice/', views.practice, name='practice'),
]