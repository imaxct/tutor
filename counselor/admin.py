from django.contrib import admin
from .models import *


# Register your models here.


class OptionInline(admin.StackedInline):
    model = Option
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': 'question_text'}),
        (u'发布日期', {'fields': 'pub_date'})
    ]
    inlines = [OptionInline]


admin.site.register(Question, QuestionAdmin)
