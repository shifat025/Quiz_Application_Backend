# Generated by Django 5.1.5 on 2025-01-21 15:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin_Management', '0004_question'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_questions', models.PositiveIntegerField(default=0)),
                ('total_attempts', models.PositiveIntegerField(default=0)),
                ('is_attempted', models.BooleanField(default=False)),
                ('quiz_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_quizzes', to='Admin_Management.quizset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
