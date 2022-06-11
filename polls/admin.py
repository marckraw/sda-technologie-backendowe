from django.contrib import admin

from polls.models import Answer, Poll, Question


class QuestionAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ('id', 'question_text', 'pub_year')
    list_display_links = ('id', 'question_text')
    list_filter = ('pub_date', )
    list_per_page = 20
    search_fields = ('question_text', )
    actions = ('cleanup_text', )
    fieldsets = [
        ("General", {
            "fields": ["id", "question_text"],
            "description": "General Info"
        }),
        ("External Information", {
            "fields": ["pub_date", "poll"],
            "description": "Additional Info"
        })
    ]
    readonly_fields = ["id", "pub_date"]

    @staticmethod
    def pub_year(obj):
        return obj.pub_date.year

    @staticmethod
    def cleanup_text(modeladmin, request, queryset):
        queryset.update(question_text='')


class AnswerAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ('id', 'answer_text', 'pub_month', )
    list_display_links = ('id', 'answer_text')
    list_filter = ('date_added', )
    list_per_page = 20
    search_fields = ('answer_text', )
    fieldsets = [
        ("General", {
            "fields": ["id", "answer_text"],
            "description": "General Info"
        }),
        ("External Information", {
            "fields": ["pub_month"],
            "description": "Additional Info"
        })
    ]
    readonly_fields = ["id", "pub_month"]

    @staticmethod
    def pub_month(obj):
        return obj.date_added.strftime('%B')

    @staticmethod
    def add_suffix(modeladmin, request, queryset):
        for obj in queryset:
            obj.answer_text += "-example"

        Answer.bulk_update(queryset)


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Poll)
admin.site.register(Question, QuestionAdmin)
