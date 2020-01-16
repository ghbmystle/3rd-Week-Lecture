from django.contrib import admin
from django.urls import path

from words2.views import get_quiz, get_result

urlpatterns = [
    path('', get_quiz, name='quiz'),
    path('result/', get_result, name='result')
]
