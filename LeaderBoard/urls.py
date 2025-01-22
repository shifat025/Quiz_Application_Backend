from django.urls import path
from .views import QuizDataApiView

urlpatterns = [
    path('quiz-data/<uuid:quizSetId>/', QuizDataApiView.as_view(), name='quiz_data')
]
