from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterCreateView(CreateView):
    model = User
    template_name = 'polls/form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("polls_views:polls-list-view")
