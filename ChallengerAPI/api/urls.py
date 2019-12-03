from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('answers/', views.AnswerList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
