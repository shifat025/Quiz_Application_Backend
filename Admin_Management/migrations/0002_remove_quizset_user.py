# Generated by Django 5.1.5 on 2025-01-20 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizset',
            name='user',
        ),
    ]
