from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('users/', views.UserExists.as_view()),
    path('answers/', views.AnswerList.as_view()),
    path('questions/', views.QuestionList.as_view()),
    path('create/', views.UserCreate.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
