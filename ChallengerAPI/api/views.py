from .models import User, SecurityQuestion, Answer
from .serializers import UserSerializer, AnswerSerializer, QuestionSerializer
from rest_framework import generics, permissions

class UserExists(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class AnswerList(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    

class QuestionList(generics.ListAPIView):
    queryset = SecurityQuestion.objects.all()
    serializer_class = QuestionSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

