from django.db import models
from django.db.models import fields
from rest_framework import serializers
from shitsumonbako.models import Question
from django.contrib.auth.models import User


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'author', 'body', 'answer', 'countReported', 'isPinned', 'isVisible', 'toUser']


class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'questions']