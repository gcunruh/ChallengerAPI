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
from rest_auth.serializers import LoginSerializer

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
    
class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='answer'
    )
    
    class Meta:
        model = SecurityQuestion
        fields = ['question', 'answers']


class AnswerSerializer(serializers.ModelSerializer):
    questions = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='question'
    )

    class Meta:
        model = Answer
        fields = ['username', 'questions', 'answer']

UserModel = get_user_model()

class CustomLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = None
    password = None

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_username(self, username):
        user = None

        if username:
            user = self.authenticate(username=username)
        else:
            msg = _('Must include username')
            raise exceptions.ValidationError(msg)
    
        return user

    def validate(self, attrs):
        username = attrs.get('username')

        user = None

        if 'allauth' in settings.INSTALLED_APPS:
            from allauth.account import app_settings

            # Authentication through email
            if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.EMAIL:
                user = self._validate_email(email, password)

            # Authentication through username
            elif app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.USERNAME:
                user = self._validate_username(username)

            # Authentication through username
            else:
                user = self._validate_username_email(username, email, password)

        else:

            if username:
                user = self._validate_username(username)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # If required, is the email verified?
        if 'rest_auth.registration' in settings.INSTALLED_APPS:
            from allauth.account import app_settings
            if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
                email_address = user.emailaddress_set.get(email=user.email)
                if not email_address.verified:
                    raise serializers.ValidationError(
                        _('E-mail is not verified.'))

        attrs['user'] = user
        return attrs
    
