from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('questions/', views.questions, name='questions'),
    path('answers/', views.answers, name='answers'),
    path('polls/', views.polls, name='polls'),

    path('hello/<int:year>/', views.hello_year, name='hello'),
    path('hello_template/<str:s0>', views.hello),
    path('animals/', views.animals)
]