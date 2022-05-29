from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import AnswerForm, NameForm, PollForm, QuestionForm
from .models import Answer, Poll, Question


def hello(request, s0):
    s1 = request.GET.get("s1", "")
    return render(
        request,
        template_name="polls/hello.html",
        context={"adjectives": [s0, s1, "beautiful", "horrible"]}
    )


def hello_year(request):
    year = request.GET.get("year", "No key in the dictionary!")
    # return HttpResponse(f"Optional argument: {year}")
    return HttpResponseRedirect(reverse("polls_views:answers-list-view"))


def animals(request):
    animals_list = request.GET.get("animals", "").split(",")
    return render(
        request,
        template_name="polls/my_template.html",
        context={"animals": animals_list}
    )


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse("IT WORKED!")
        return render(
            request,
            template_name="polls/form.html",
            context={"form": form}
        )
    return render(
        request,
        template_name="polls/form.html",
        context={"form": NameForm()}
    )


def index(request):
    return render(
        request,
        template_name="polls/index.html"
    )


@login_required
def polls(request):
    return render(
        request,
        template_name="polls/polls.html",
        context={"polls": Poll.objects.all()}
    )


def answers(request):
    return render(
        request,
        template_name="polls/answers.html",
        context={"answers": Answer.objects.all()}
    )


def questions(request):
    return render(
        request,
        template_name="polls/questions.html",
        context={"questions": Question.objects.all()}
    )


def poll_form(request):
    form = PollForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data["name"]
        Poll.objects.create(name=name)
        return render(
            request,
            template_name="polls/polls.html",
            context={"polls": Poll.objects.all()}
        )
    return render(
        request,
        template_name="polls/form.html",
        context={"form": form}
    )


def question_form(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question_text = form.cleaned_data["question_text"]
        poll = form.cleaned_data["poll"]
        Question.objects.create(question_text=question_text, poll=poll)
        return HttpResponse("IT WORKED")
    return render(
        request,
        template_name="polls/form.html",
        context={"form": form}
    )


def answer_form(request):
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        answer_text = form.cleaned_data["answer_text"]
        Answer.objects.create(answer_text=answer_text)
        return HttpResponse("IT WORKED")
    return render(
        request,
        template_name="polls/form.html",
        context={"form": form}
    )