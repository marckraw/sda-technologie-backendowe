from django.urls import path

from . import views

urlpatterns = [
    path('hello/<int:year>/', views.hello, name='hello')
]