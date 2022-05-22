import pytz
from django.core.exceptions import ValidationError
from django.forms import CharField, Form, DateTimeField, ModelChoiceField
from datetime import datetime
from .models import Poll

utc = pytz.UTC


class PastMonthField(DateTimeField):
    def validate(self, value):
        super().validate(value)
        if value >= datetime.today().replace(tzinfo=utc):
            raise ValidationError('Only past dates allowed here.')


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


class NameForm(Form):
    name = CharField(max_length=128)
    birth_date = DateTimeField()


class PollForm(Form):
    name = CharField(max_length=128)


class QuestionForm(Form):
    question_text = CharField(max_length=128, validators=[capitalized_validator])
    pub_date = PastMonthField(label='Publication Date')
    poll = ModelChoiceField(queryset=Poll.objects.all())
