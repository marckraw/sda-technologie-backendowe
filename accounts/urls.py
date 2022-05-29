from django.urls import include, path

from accounts.views_class import RegisterCreateView

urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name='register'),
]
