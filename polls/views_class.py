from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    ListView,
    TemplateView,
    UpdateView
)
from django.urls import reverse, reverse_lazy


from polls.forms import (
    AnswerForm,
    AnswerModelForm,
    PollForm,
    PollModelForm,
    QuestionForm,
    QuestionModelForm
)
from polls.models import Answer, Poll, Question


class PollView(View):
    def get(self, request):
        return render(
            request,
            template_name="polls/polls.html",
            context={"polls": Poll.objects.all()}
        )


class PollTemplateView(TemplateView):
    template_name = "polls/polls.html"
    extra_context = {"polls": Poll.objects.all()}


class PollFormView(FormView):
    template_name = "polls/form.html"
    form_class = PollForm
    success_url = reverse_lazy("polls_views:polls-list-view")

    def form_valid(self, form):
        result = super().form_valid(form)
        name = form.cleaned_data["name"]
        Poll.objects.create(name=name)
        return result


class PollModelFormView(FormView):
    template_name = "polls/form.html"
    form_class = PollModelForm
    success_url = reverse_lazy("polls_views:polls-list-view")

    def form_valid(self, form):
        result = super().form_valid(form)
        form.save()
        return result


class PollListView(ListView):
    template_name = "polls/list_view.html"
    model = Poll


class PollCreateView(CreateView):
    model = Poll
    fields = "__all__"
    template_name = "polls/form.html"
    success_url = reverse_lazy("polls_views:polls-list-view")


class PollDetailView(DetailView):
    model = Poll
    template_name = "polls/my_poll.html"


class PollUpdateView(UpdateView):
    model = Poll
    fields = ("name", )
    template_name = "polls/form.html"
    success_url = reverse_lazy("polls_views:polls-list-view")


class PollDeleteView(DeleteView):
    model = Poll
    template_name = "polls/delete.html"
    success_url = reverse_lazy("polls_views:poll-list-view")


class QuestionView(View):
    def get(self, request):
        return render(
            request,
            template_name="polls/questions.html",
            context={"questions": Question.objects.all()}
        )

    def post(self, request):
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            question_text = form.cleaned_data["question_text"]
            poll = form.cleaned_data["poll"]
            Question.objects.create(question_text=question_text, poll=poll)
            return HttpResponseRedirect(reverse("polls_views:questions-list-view"))
        return render(
            request,
            template_name="polls/form.html",
            context={"form": form}
        )


class QuestionUpdateView(View):
    def get(self, request, pk):
        return render(
            request,
            template_name="polls/form.html",
            context={"form": QuestionForm()}
        )

    def post(self, request, pk):
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            q = get_object_or_404(Question, pk=pk)
            q.question_text = form.cleaned_data["question_text"]
            q.poll = form.cleaned_data["poll"]
            q.save()
            return HttpResponseRedirect(reverse("polls_views:questions-list-view"))
        return render(
            request,
            template_name="polls/form.html",
            context={"form": form}
        )


class QuestionUpdateGenericView(UpdateView):
    model = Question
    fields = ("question_text", )
    template_name = "polls/form.html"
    success_url = reverse_lazy("polls_views:questions-list-view")


class QuestionDetailView(View):
    def get(self, request, pk):
        return render(
            request,
            template_name="polls/my_question.html",
            context={"question": get_object_or_404(Question, pk=pk)}
        )


class QuestionDeleteView(View):
    def get(self, request, pk):
        return render(
            request,
            template_name="polls/delete.html",
            context={"question": get_object_or_404(Question, pk=pk)}
        )

    def post(self, request, pk):
        Question.objects.get(pk=pk).delete()
        return HttpResponseRedirect(reverse("polls_views:questions-list-view"))


class QuestionDeleteGenericView(DeleteView):
    model = Question
    template_name = "polls/delete.html"
    success_url = reverse_lazy("polls_views:questions-list-view")


class QuestionDetailGenericView(DetailView):
    model = Question
    template_name = "polls/my_question.html"


class QuestionCreateView(CreateView):
    model = Question
    fields = "__all__"
    template_name = "polls/form.html"
    success_url = reverse_lazy("polls_views:questions-list-view")


class QuestionTemplateView(TemplateView):
    template_name = "polls/questions.html"
    extra_context = {"questions": Question.objects.all()}


class QuestionFormView(FormView):
    template_name = "polls/form.html"
    form_class = QuestionForm
    success_url = reverse_lazy("polls_views:questions-list-view")

    def form_valid(self, form):
        result = super().form_valid(form)
        question_text = form.cleaned_data["question_text"]
        poll = form.cleaned_data["poll"]
        Question.objects.create(question_text=question_text, poll=poll)
        return result


class QuestionModelFormView(FormView):
    template_name = "polls/form.html"
    form_class = QuestionModelForm
    success_url = reverse_lazy("polls_views:questions-list-view")

    def form_valid(self, form):
        result = super().form_valid(form)
        form.save()
        return result


class QuestionListView(ListView):
    template_name = "polls/list_view.html"
    model = Question


class AnswerView(View):
    def get(self, request):
        return render(
            request,
            template_name="polls/answers.html",
            context={"answers": Answer.objects.all()}
        )


class AnswerTemplateView(TemplateView):
    template_name = "polls/answers.html"
    extra_context = {"answers": Answer.objects.all()}


class AnswerFormView(FormView):
    template_name = "polls/form.html"
    form_class = AnswerForm
    success_url = reverse_lazy("polls_views:answers-list-view")

    def form_valid(self, form):
        result = super().form_valid(form)
        answer_text = form.cleaned_data["answer_text"]
        question = form.cleaned_data["question"]
        Answer.objects.create(answer_text=answer_text, question=question)
        return result


class AnswerModelFormView(FormView):
    template_name = "polls/form.html"
    form_class = AnswerModelForm
    success_url = reverse_lazy("polls_views:answers-list-view")

    def form_valid(self, form):
        result = super().form_valid(form)
        form.save()
        return result


class AnswerListView(ListView):
    template_name = "polls/list_view.html"
    model = Answer


class AnswerCreateView(CreateView):
    model = Answer
    fields = "__all__"
    template_name = "polls/form.html"
    success_url = reverse_lazy("polls_views:answers-list-view")


class AnswerDetailView(DetailView):
    model = Answer
    template_name = "polls/my_answer.html"


class AnswerUpdateView(UpdateView):
    model = Answer
    fields = ("name",)
    template_name = "polls/form.html"
    success_url = reverse_lazy("polls_views:answers-list-view")


class AnswerDeleteView(DeleteView):
    model = Answer
    template_name = "polls/delete.html"
    success_url = reverse_lazy("polls_views:answers-list-view")

