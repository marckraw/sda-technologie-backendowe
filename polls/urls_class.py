from django.urls import path

from . import views_class

urlpatterns = [
    path("polls-class-view", views_class.PollView.as_view(), name="polls-class-view"),
    path("polls-template-view", views_class.PollTemplateView.as_view(), name="polls-template-view"),
    path("polls-list-view", views_class.PollListView.as_view(), name="polls-list-view"),

    path("answers-class-view", views_class.AnswerView.as_view(), name="answers-class-view"),
    path("answers-template-view", views_class.AnswerTemplateView.as_view(), name="answers-template-view"),
    path("answers-list-view", views_class.AnswerListView.as_view(), name="answers-list-view"),

    path("questions-class-view", views_class.QuestionView.as_view(), name="questions-class-view"),
    path("questions-template-view", views_class.QuestionTemplateView.as_view(), name="questions-template-view"),
    path("questions-list-view", views_class.QuestionListView.as_view(), name="questions-list-view"),
]