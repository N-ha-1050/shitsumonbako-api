from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render

# Create your views here.
from shitsumonbako.models import Question
from shitsumonbako.serializers import QuestionSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer