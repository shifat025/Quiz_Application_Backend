from django.db import models
from Admin_Management.models import QuizSet
from django.contrib.auth.models import User


# Create your models here.
class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_set = models.ForeignKey(QuizSet, on_delete=models.CASCADE, related_name='user_quizzes')
    total_questions = models.PositiveIntegerField(default=0)
    total_attempts = models.PositiveIntegerField(default=0)
    is_attempted = models.BooleanField(default=False)
    submitted_answers = models.JSONField(default=dict)
