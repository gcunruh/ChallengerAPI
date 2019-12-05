from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from api.backupcodegen import id_generator
from django.utils import timezone
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'users'
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 50, unique=True, null=False)
    email = models.EmailField(max_length=50, unique=True, null=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    backup1 = models.CharField(max_length=15, default=id_generator())
    backup2 = models.CharField(max_length=15, default=id_generator())
    backup3 = models.CharField(max_length=15, default=id_generator())

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS=[]

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class SecurityQuestion(models.Model):
    class Meta:
        db_table = 'security_question'
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length = 250, null=False)

class Answer(models.Model):
    class Meta:
        db_table = 'answers'
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='answers', on_delete=models.CASCADE)
    security_question = models.ForeignKey(SecurityQuestion, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=250, null=False)

    @property
    def question(self):
        return self.security_question.question

    @property
    def username(self):
        return self.user.username
