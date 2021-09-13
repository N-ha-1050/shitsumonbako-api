from django.urls import path
from shitsumonbako import views


urlpatterns = [
    path('questions/', views.question_list),
    path('questions/<int:pk>/', views.question_detail),
]