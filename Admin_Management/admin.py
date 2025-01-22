# from django.contrib import admin
# from .models import QuizSet

# # Register your models here.
# admin.site.register(QuizSet)

from django.contrib import admin
from .models import QuizSet, Question

@admin.register(QuizSet)
class QuizSetAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'created_at')
    search_fields = ('title', 'description')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'quiz_set', 'marks', 'created_at')
    search_fields = ('question',)
