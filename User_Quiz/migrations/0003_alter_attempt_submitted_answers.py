# Generated by Django 5.1.5 on 2025-01-22 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Quiz', '0002_attempt_submitted_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='submitted_answers',
            field=models.JSONField(default=dict),
        ),
    ]
