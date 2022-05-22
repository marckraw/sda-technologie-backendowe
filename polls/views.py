from django.http import HttpResponse
from django.shortcuts import render
from .models import Poll, Answer, Question
from .forms import NameForm, PollForm, QuestionForm


def question_form(request):
    form = QuestionForm(request.POST or None)

    if form.is_valid():
        question_text = form.cleaned_data['question_text']
        pub_date = form.cleaned_data['pub_date']
        poll = form.cleaned_data['poll']
        Question.objects.create(
            question_text=question_text,
            pub_date=pub_date,
            poll=poll
        )
        return HttpResponse("It Worked!")

    return render(
        request,
        template_name="polls/form.html",
        context={'form': form}
    )

def poll_form(request):
    form = PollForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data["name"]
        Poll.objects.create(name=name)
        return HttpResponse("It Worked!")

    return render(
        request,
        template_name="polls/form.html",
        context={'form': form}
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
        template_name='polls/index.html'
    )


def polls(request):
    print("twoja stara")
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


def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='polls/hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )


def animals(request):
    animals_list = request.GET.get('animals', '')

    return render(
        request, template_name="polls/animals.html",
        context={'animals': animals_list.split(",")}
    )


def hello_year(request, year):
    return HttpResponse(f"Hello, world! {year}")


