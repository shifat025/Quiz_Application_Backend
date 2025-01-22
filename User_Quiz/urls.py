from django.urls import path

from .views import UserQuizSetView ,GetQuizView, SubmitQuizView

urlpatterns = [
    path('user_set/', UserQuizSetView.as_view(), name='user_quiz_set'),
    path('quizzes/<uuid:id>/', GetQuizView.as_view(), name='get_quiz'),
    path('submit-quiz/<uuid:quizSetId>/', SubmitQuizView.as_view(), name='submit_quiz')

]
