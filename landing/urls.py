"""Цей файл містить змінну urlpatterns, яка є списком шляхів URL."""

from django.urls import path
from landing.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
