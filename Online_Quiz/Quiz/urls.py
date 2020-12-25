from django.urls import path
from . import views

urlpatterns = [
    path('start_quiz', views.start_quiz, name='start_quiz'),
    path('quiz', views.quiz, name='quiz'),
    path('quiz2', views.quiz2, name='quiz2'),  
]
