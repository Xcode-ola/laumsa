from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(contact_details)
admin.site.register(CourseList)
admin.site.register(Quiz)
admin.site.register(PracticeQuestion)
admin.site.register(ChapterList)
admin.site.register(CourseSummary)

class AnswerInLineTable(admin.TabularInline):
    model = Answer
    fields = [
        'choice',
        'correct',
    ]

class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'quiz',
        'question',
    ]
    list_display = [
        'quiz',
        'question',
    ]
    inlines = [
        AnswerInLineTable,
    ]

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'choice',
        'correct'
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)