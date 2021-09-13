from django.urls import path
from shitsumonbako import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('questions/', views.question_list),
    path('questions/<int:pk>/', views.question_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns)