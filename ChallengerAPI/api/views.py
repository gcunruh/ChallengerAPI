from .models import User, SecurityQuestion, Answer
from .serializers import UserSerializer, AnswerSerializer
from rest_framework import generics

class UserList(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
