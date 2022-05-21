from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        if self.name:
            return self.name
        return '-- It doesnt have name --'


class Question(models.Model):
    question_text = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="questions", null=True, blank=True)

    def __str__(self):
        if self.question_text:
            return self.question_text
        return '-- It doesnt have question_text --'


class Answer(models.Model):
    answer_text = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers", null=True, blank=True)

    def __str__(self):
        if self.answer_text:
            return self.answer_text
        return '-- It doesnt have answer_text --'

