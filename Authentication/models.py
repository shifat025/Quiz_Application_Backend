from django.contrib.auth.models import User
from django.db import models

class Role(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='role')
    role = models.BooleanField(default=False,blank=True, null=True)  # Extra field for manager

    def __str__(self):
        return f"{self.user.username} - {'Admin' if self.role else 'User'}"
