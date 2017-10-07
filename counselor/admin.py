from django.contrib import admin
from .models import *


# Register your models here.


class OptionInline(admin.StackedInline):
    model = Option
    can_delete = True
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text')
    inlines = [OptionInline]


class AcademyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stu_no', 'id_no', 'grade', 'academy')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'academy')


class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'option_num', 'option_text', 'score')


admin.site.register(Question, QuestionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Record)
admin.site.register(Academy, AcademyAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Option, OptionAdmin)
