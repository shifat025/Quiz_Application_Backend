# Generated by Django 5.1.5 on 2025-01-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizset',
            name='total_attempts',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
