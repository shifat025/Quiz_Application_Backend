from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .models import QuizSet, Question
from .serializers import QuizSetCreateSerializer, QuizSetDetailSerializer, QuestionSerializer
from rest_framework.permissions import IsAuthenticated
from Authentication.permissions import IsAdminRole

class QuizSetCreateView(CreateAPIView):
    queryset = QuizSet.objects.all()
    serializer_class = QuizSetCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]  # Ensure the user is authenticated

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set the user from the request


class QuizSetListView(ListAPIView):
    queryset = QuizSet.objects.all()
    serializer_class = QuizSetDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]  # Ensure the user is authenticated

    def get_queryset(self):
        # Ensure the user can only update their own QuizSets
        return QuizSet.objects.filter(user=self.request.user)


class QuizSetUpdateView(UpdateAPIView):
    queryset = QuizSet.objects.all()
    serializer_class = QuizSetCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get_queryset(self):
        # Ensure the user can only update their own QuizSets
        return QuizSet.objects.filter(user=self.request.user)


class QuizSetDeleteView(DestroyAPIView):
    queryset = QuizSet.objects.all()
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get_queryset(self):
        # Ensure the user can only delete their own QuizSets
        return QuizSet.objects.filter(user=self.request.user)


class QuestionUpdateView(UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get_queryset(self):
        # Ensure the user can only update questions within their own QuizSets
        return Question.objects.filter(quiz_set__user=self.request.user)


class AddQuestion(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]

    def perform_create(self, serializer):
        quizSetId = self.kwargs['quizSetId']
        quizset = QuizSet.objects.get(id = quizSetId, user = self.request.user)
        serializer.save(quiz_set = quizset)


class QuestionUpdateView(UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get_queryset(self):
        # Ensure the user can only update questions within their own QuizSets
        return Question.objects.filter(quiz_set__user=self.request.user)


class QuestionDeleteView(DestroyAPIView):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get_queryset(self):
        # Ensure the user can only delete questions within their own QuizSets
        return Question.objects.filter(quiz_set__user=self.request.user)
    
