from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Attempt
from rest_framework import status
from .serializers import UserQuizSetSerializer, GetQuizSerializer
from Admin_Management.models import QuizSet
from rest_framework.permissions import IsAuthenticated


class UserQuizSetView(ListAPIView):
    serializer_class = UserQuizSetSerializer
    queryset = QuizSet.objects.all()

    def get_queryset(self):
        return QuizSet.objects.filter(status='published')  # Filter queryset to include only published QuizSets

class GetQuizView(APIView):
    def get(self, request, id):
        try:
            quiz_set = QuizSet.objects.get(id = id)
        except QuizSet.DoesNotExist:
            return Response({"error": "Quiz set not found"}, status=404)
        
        # Serialize the QuizSet with questions
        serializer = GetQuizSerializer(quiz_set)
        return Response(serializer.data)
    

class SubmitQuizView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, quizSetId):
        try:
            
            quiz_set = QuizSet.objects.get(id = quizSetId)
            user = request.user

            answers = request.data.get("answers", {})
            
            if not answers:
                return Response(
                    {"error": "Answers are required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            attempt , created = Attempt.objects.get_or_create(
                user = user,
                quiz_set = quiz_set,
                )
            attempt.submitted_answers = answers if answers else {}
            attempt.is_attempted = True
            attempt.total_attempts += 1
            attempt.save()

            return Response(
                {
                    "message": "Answers submitted successfully!",
                    "is_attempted": attempt.is_attempted,
                    "total_attempts": attempt.total_attempts,
                },
                status=status.HTTP_200_OK,
            )
            
        except QuizSet.DoesNotExist:
            return Response(
                {"error": "Quiz not found."}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


