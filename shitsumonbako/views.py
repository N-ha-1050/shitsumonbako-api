from django.shortcuts import render

# Create your views here.
from shitsumonbako.models import Question
from shitsumonbako.serializers import QuestionSerializer
from rest_framework import generics


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer