from django.db import models
from django.shortcuts import render

# Create your views here.
from shitsumonbako.models import Question
from shitsumonbako.serializers import QuestionSerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from shitsumonbako.permissions import IsToUserOrReadOnly, UserOnly
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'questions': reverse('question-list', request=request, format=format),
    })


class QuestionList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsToUserOrReadOnly]


class QuestionReport(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Question.objects.all()
    #serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        question = self.get_object()
        question.report()
        serializer = QuestionSerializer(question)
        return Response(serializer.data)


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, UserOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserQuestionList(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, UserOnly]

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        questions = Question.objects.filter(toUser=user, isVisible=True)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)