from rest_framework import serializers
from .models import Attempt
from Admin_Management.models import QuizSet
from Admin_Management.serializers import QuestionSerializer
 
class UserQuizSetSerializer(serializers.ModelSerializer):
    total_questions = serializers.SerializerMethodField()
    total_attempts = serializers.SerializerMethodField()
    is_attempted = serializers.SerializerMethodField()

    class Meta:
        model = QuizSet
        fields = ['id', 'title', 'description', 'thumbnail', 'status', 'created_at', 'total_questions', 'total_attempts', 'is_attempted']

    def get_total_questions(self, obj):
        return obj.question.count()
    
    def get_total_attempts(self, obj):
        return Attempt.objects.filter(quiz_set=obj).count()
    
    def get_is_attempted(self, obj):
        request = self.context.get('request')
        user = request.user if request else None
        if user and user.is_authenticated:
            return Attempt.objects.filter(quiz_set = obj, user = user).exists()
        return False
    

class GetQuizSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    total_attempts = serializers.IntegerField(read_only = True)
     
    class Meta:
        model = QuizSet
        fields = ['id', 'title', 'description', 'created_at',  'questions','total_attempts']

    def get_questions(self, obj):
        # Get only questions for the specific QuizSet
        questions = obj.question.all()
        return QuestionSerializer(questions, many=True).data

    
    
