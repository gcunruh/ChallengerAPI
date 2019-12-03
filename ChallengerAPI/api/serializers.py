from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError
from rest_auth.models import TokenModel
from rest_auth.utils import import_callable
from .models import User, SecurityQuestion, Answer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.contrib.auth import get_user_model, authenticate
from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text
from django.conf import settings

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()

    class Meta:
        model = Answer
        fields = ['username', 'question', 'answer']

    
