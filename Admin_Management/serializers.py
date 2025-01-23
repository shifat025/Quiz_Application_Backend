from rest_framework import serializers
from .models import QuizSet, Question

# Serializer for questions
class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    quizSetId = serializers.PrimaryKeyRelatedField(read_only = True, source='quiz_set')
    created_at = serializers.DateTimeField(read_only = True)
    marks = serializers.IntegerField(default = 5)

    class Meta:
        model = Question
        fields = ['id', 'quizSetId', 'question', 'options', 'correct_answer','marks','created_at']


# Serializer for QuizSet GET requests (includes questions)
class QuizSetDetailSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    status = serializers.CharField(read_only=True)
    thumbnail = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    Questions = serializers.SerializerMethodField()  # Custom method for questions
    userId = serializers.PrimaryKeyRelatedField(read_only=True, source='user')

    class Meta:
        model = QuizSet
        fields = ['id', 'title', 'description', 'status', 'thumbnail', 'created_at', 'userId', 'Questions']

    def get_Questions(self, obj):
        # Get only questions for the specific QuizSet
        questions = obj.question.all()
        return QuestionSerializer(questions, many=True).data
    

    

class QuizSetCreateSerializer(serializers.ModelSerializer):
    # Add read-only fields
    id = serializers.UUIDField(read_only=True)  # UUID field for the ID
    status = serializers.CharField(read_only=True)
    thumbnail = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = QuizSet
        fields = ['id', 'title', 'description', 'status', 'thumbnail', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Check if this is an update (PATCH/PUT) request
        if self.context['request'].method in ['PUT', 'PATCH']:
            self.fields['status'].read_only = False  # Allow `status` to be updated

    def validate(self, attrs):
        # Validate that the quiz set has at least one question before publishing.
        if self.instance:  # If updating
            if attrs.get('status') == 'published' and self.instance.question.count() == 0:
                raise serializers.ValidationError(
                    {"error": "Cannot publish a QuizSet with no questions."}
                )
        return attrs
