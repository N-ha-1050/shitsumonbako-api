from django.urls import path
from shitsumonbako import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.api_root),
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/<int:pk>/questions/', views.UserQuestionList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)