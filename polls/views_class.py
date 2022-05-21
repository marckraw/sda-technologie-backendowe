from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from polls.models import Poll, Answer, Question


class PollView(View):
    def get(self, request):
        return render(
            request,
            template_name="polls.html",
            context={"polls": Poll.objects.all()}
        )


class PollTemplateView(TemplateView):
    template_name = 'polls.html'
    extra_context = {"polls": Poll.objects.all()}


class PollListView(ListView):
    template_name = 'list-view.html'
    model = Poll


class AnswerView(View):
    def get(self, request):
        return render(
            request,
            template_name="answers.html",
            context={"answers": Answer.objects.all()}
        )

class AnswerTemplateView(TemplateView):
    template_name = 'answers.html'
    extra_context = {"answers": Answer.objects.all()}

class AnswerListView(ListView):
    template_name = 'list-view.html'
    model = Answer

class QuestionView(View):
    def get(self, request):
        return render(
            request,
            template_name="questions.html",
            context={"questions": Question.objects.all()}
        )

class QuestionTemplateView(TemplateView):
    template_name = 'questions.html'
    extra_context = {"questions": Question.objects.all()}

class QuestionListView(ListView):
    template_name = 'list-view.html'
    model = Question




