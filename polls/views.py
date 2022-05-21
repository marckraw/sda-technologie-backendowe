from django.http import HttpResponse
from django.shortcuts import render
from .models import Poll, Answer, Question


def index(request):
    return render(
        request,
        template_name='index.html'
    )


def polls(request):
    return render(
        request,
        template_name="polls.html",
        context={"polls": Poll.objects.all()}
    )


def answers(request):
    return render(
        request,
        template_name="answers.html",
        context={"answers": Answer.objects.all()}
    )


def questions(request):
    return render(
        request,
        template_name="questions.html",
        context={"questions": Question.objects.all()}
    )


def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )


def animals(request):
    animals_list = request.GET.get('animals', '')

    return render(
        request, template_name="animals.html",
        context={'animals': animals_list.split(",")}
    )


def hello_year(request, year):
    return HttpResponse(f"Hello, world! {year}")


