from django.views import View
from django.http import JsonResponse, QueryDict
from django.core import serializers

from polls.models import Question, Answer


class QuestionList(View):
    def get(self, request):
        questions = Question.objects.all().values('id', 'question_text', 'pub_date')
        question_list = list(questions)

        return JsonResponse({
            "questions": question_list
        })

    def post(self, request):
        question_text = request.POST.get('question_text', '')
        poll_id = request.POST.get('poll_id', '')

        question = Question.objects.create(question_text=question_text, poll_id=poll_id)

        return JsonResponse(
            {
                "id": question.id,
                "question_text": question.question_text,
                "pub_date": question.pub_date
            },
            status=201
        )


class QuestionDetail(View):
    def get(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return JsonResponse(
                {
                    "error": f"Object with pk {pk} does not exist!"
                },
                status=404
            )

        return JsonResponse(
            {
                "id": question.id,
                "question_text": question.question_text,
                "pub_date": question.pub_date
            }
        )

    def delete(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return JsonResponse(
                {
                    "error": f"Object with pk {pk} does not exist!"
                },
                status=404
            )

        question.delete()

        return JsonResponse({}, 200)

    def put(self, request, pk):
        body = QueryDict(request.body)
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return JsonResponse(
                {"error": f"Question with id {pk} does not exist!"},
                status=404
            )
        question.question_text = body["question_text"]
        question.save(update_fields=["question_text"])
        return JsonResponse(
            {
                "id": question.id,
                "question_text": question.question_text,
                "pub_date": question.pub_date
            }
        )

class AnswerList(View):
    def get(self, request):
        answers = Answer.objects.all().values('id', 'answer_text', 'date_added')
        answer_list = list(answers)

        response_data = {
            "answers": answer_list
        }

        return JsonResponse(response_data, status=200)

    def post(self, request):
        answer_text = request.POST.get('answer_text', '')
        question_id = request.POST.get('question_id', 1)

        answer = Answer.objects.create(answer_text=answer_text, question_id=question_id)

        response_data = {
            "id": answer.id,
            "answer_text": answer.answer_text,
            "date_added": answer.date_added
        }

        return JsonResponse(
            response_data,
            status=201
        )


class AnswerDetail(View):
    def get(self, request, pk):
        try:
            answer = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            return JsonResponse(
                {
                    "error": f"Object with pk {pk} does not exist!"
                },
                status=404
            )

        response_data = {
            "id": answer.id,
            "answer_text": answer.answer_text,
            "date_added": answer.date_added
        }

        return JsonResponse(
            response_data,
            status=200
        )

    def delete(self, request, pk):
        try:
            answer = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            return JsonResponse(
                {
                    "error": f"Object with pk {pk} does not exist!"
                },
                status=404
            )

        answer.delete()

        return JsonResponse({}, status=200)

    def put(self, request, pk):
        body = QueryDict(request.body)
        try:
            answer = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            return JsonResponse(
                {"error": f"Answer with id {pk} does not exist!"},
                status=404
            )
        answer.answer_text = body["answer_text"]
        answer.save(update_fields=["answer_text"])
        return JsonResponse(
            {
                "id": answer.id,
                "answer_text": answer.answer_text,
                "date_added": answer.date_added
            }
        )

