from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from User_Quiz.models import Attempt
from rest_framework import status
from Admin_Management.models import QuizSet, Question
from rest_framework.permissions import IsAuthenticated


class QuizDataApiView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request , quizSetId):
        quiz_set = get_object_or_404(QuizSet, id= quizSetId) # Get the quiz set by its ID or return a 404 error if not found
        
        # Fetch all attempts and questions related to the quiz set
        attempts = Attempt.objects.filter(quiz_set = quiz_set)
        corrects = Question.objects.filter(quiz_set = quiz_set)

        # Prepare the main response structure
        data = {
            "quiz": {
                "id": str(quiz_set.id),
                "title": quiz_set.title,
                "description": quiz_set.description,
                "total_marks": quiz_set.question.count() * 5,
                "total_questions": quiz_set.question.count()
            },
            "stats":{
                "tatal_attempts": attempts.count()
            },
            "attempts": []
        }
        
        # Store correct answers for all questions in the quiz set
        correct_answers =[]
        for correct in corrects:
            correct_answers.append({"question_id": str(correct.id),"answer": correct.correct_answer, "marks": correct.marks})


         # Process each attempt and add its details to the response
        for attempt in attempts:
            user_data = {
                "id": str(attempt.user.id),
                "full_name": f"{attempt.user.first_name} {attempt.user.last_name}",
                "email": attempt.user.email
            }

            # Collect the answers submitted by the user
            submitted_answers =[]
            for question_id, answer in attempt.submitted_answers.items():
                submitted_answers.append({"question_id":str(question_id), "answer": answer})

           
            # Prepare data for this attempt
            attempt_data = {
                "id": str(attempt.id),
                "user": user_data,
                "submitted_answers": submitted_answers,
                "correct_answers": correct_answers
            }

             # Add this attempt's data to the list
            data["attempts"].append(attempt_data)

        # Return  final response with all data
        return Response(data, status=status.HTTP_200_OK)