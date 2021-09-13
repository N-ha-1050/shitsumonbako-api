from django.db.models import fields
from rest_framework import serializers
from shitsumonbako.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'author', 'body', 'answer', 'countReported', 'isPinned', 'isVisible']#['toUser']
