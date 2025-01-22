from django.urls import path
from .views import (
    QuizSetCreateView, QuizSetListView, AddQuestion,
    QuizSetUpdateView, QuizSetDeleteView,
    QuestionUpdateView, QuestionDeleteView
)

urlpatterns = [
    path('quizsets/create/', QuizSetCreateView.as_view(), name='quizset-create'),
    path('quizsets/', QuizSetListView.as_view(), name='quizset-list'),
    path('quizsets/<uuid:quizSetId>/questions/', AddQuestion.as_view(), name='add-question-to-quizset'),
    path('quizsets/<uuid:pk>/update/', QuizSetUpdateView.as_view(), name='quizset-update'),  # PATCH: Update QuizSet
    path('quizsets/<uuid:pk>/delete/', QuizSetDeleteView.as_view(), name='quizset-delete'),  # DELETE: Delete QuizSet
    path('questions/<uuid:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),  # PATCH: Update Question
    path('questions/<uuid:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),  # DELETE: Delete Question
]
