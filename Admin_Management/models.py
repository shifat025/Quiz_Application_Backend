from django.db import models
from django.contrib.auth.models import User
import uuid
import random
import os

STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
       ]

class QuizSet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quzsets')
    title = models.CharField(max_length=210)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    thumbnail = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generate a random image from the static directory
        if not self.thumbnail:
            image_dir = os.path.join('static', 'images')
            image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
            if image_files:
                random_image = random.choice(image_files)
                self.thumbnail = f'/static/images/{random_image}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.status}"
    

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz_set = models.ForeignKey(QuizSet, on_delete=models.CASCADE, related_name='question')
    question = models.CharField(max_length=255)
    options = models.JSONField()
    correct_answer = models.CharField(max_length=255)
    marks = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)